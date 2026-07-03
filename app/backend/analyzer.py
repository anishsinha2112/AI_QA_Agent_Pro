
def classify_failure(log):
    log = log.lower()

    if "500" in log:
        return "Developer Bug: Backend/API failure"
    if "timeout" in log:
        return "Automation/Environment Issue"
    if "no such element" in log:
        return "Automation Issue: Locator changed"
    if "element click intercepted" in log:
        return "Possible application UI overlay or synchronization issue"

    return "Needs investigation"
