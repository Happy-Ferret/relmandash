def getAssignedOptions(emails):
    options = {
        'email1':            emails,
        'email1_type':       'contains_any_words',
        'email1_assigned_to':1,
        'order':             'Last Changed',
        'field0-0-0':        'status',
        'type0-0-0':         'equals',
        'value0-0-0':        'NEW',
        'field0-0-1':        'status',
        'type0-0-1':         'equals',
        'value0-0-1':        'ASSIGNED',
        'field0-0-2':        'status',
        'type0-0-2':         'equals',
        'value0-0-2':        'REOPENED',
        'field0-0-3':        'status',
        'type0-0-3':         'equals',
        'value0-0-3':        'UNCONFIRMED',
        'include_fields':    '_all',
    }
    return options
    
def getToFollowUp(emails, beta, aurora):
    options = {
        'email1':           emails,
        'email1_type':      'contains_any_words',
        'email1_assigned_to':        1,
        'order':            'Last Changed',
        'negate0':          1,
        'field0-0-0':       'cf_tracking_firefox'+str(beta),
        'type0-0-0':        'not_equals',
        'value0-0-0':       '+',
        'field0-0-1':       'cf_status_firefox'+str(beta),
        'type0-0-1':        'contains_any_words',
        'value0-0-1':       'fixed, wontfix, unaffected, verified, disabled',
        'field0-1-0':       'cf_tracking_firefox'+str(beta),
        'type0-1-0':        'equals',
        'value0-1-0':       '+',
        'field0-1-1':       'cf_status_firefox'+str(beta),
        'type0-1-1':        'not_equals',
        'value0-1-1':       'affected',
        'field0-2-0':       'cf_tracking_firefox'+str(aurora),
        'type0-2-0':        'not_equals',
        'value0-2-0':       '+',
        'field0-2-1':       'cf_status_firefox'+str(aurora),
        'type0-2-1':        'contains_any_words',
        'value0-2-1':       'fixed, wontfix, unaffected, verified, disabled',
        'field0-3-0':       'cf_tracking_firefox'+str(aurora),
        'type0-3-0':        'equals',
        'value0-3-0':       '+',
        'field0-3-1':       'cf_status_firefox'+str(aurora),
        'type0-3-1':        'not_equals',
        'value0-3-1':       'affected',
        'include_fields':   '_default,attachments',
    }
    return options
    
def getNeedsInfo(emails):
    options = {
        'field0-0-0':       'requestees.login_name',
        'type0-0-0':        'contains_any_words',
        'value0-0-0':       emails,
        'include_fields':   '_all',
    }
    return options
    
def getProdComp(product, components, beta, aurora, esr):
    options = {
        'product':           product,
        'order':             'Last Changed',
        'field0-0-0':        'status',
        'type0-0-0':         'equals',
        'value0-0-0':        'NEW',
        'field0-0-1':        'status',
        'type0-0-1':         'equals',
        'value0-0-1':        'ASSIGNED',
        'field0-0-2':        'status',
        'type0-0-2':         'equals',
        'value0-0-2':        'REOPENED',
        'field0-0-3':        'status',
        'type0-0-3':         'equals',
        'value0-0-3':        'UNCONFIRMED',
        'field0-1-0':        'cf_tracking_firefox' + str(beta),
        'type0-1-0':         'equals',
        'value0-1-0':        '+',
        'field0-1-1':        'cf_tracking_firefox' + str(aurora),
        'type0-1-1':         'equals',
        'value0-1-1':        '+',
        'field0-1-2':        'cf_tracking_firefox' + str(esr),
        'type0-1-2':         'equals',
        'value0-1-2':        '+',
        'field1-0-0':        'component',
        'type1-0-0':         'contains_any_words',
        'value1-0-0':        components,
        'include_fields':    '_all',
    }
    return options
