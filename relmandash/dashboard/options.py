def getAssignedOptions(emails, vt):
    options = {
        'email1':            emails,
        'email1_type':       'contains_any_words',
        'email1_assigned_to': 1,
        'field0-0-0':        'status',
        'type0-0-0':         'contains_any_words',
        'value0-0-0':        'NEW, ASSIGNED, REOPENED, UNCONFIRMED',
        'field1-0-0':        'cf_tracking_firefox'+str(vt.beta),
        'type1-0-0':         'equals',
        'value1-0-0':        '+',
        'field1-0-1':        'cf_tracking_firefox'+str(vt.aurora),
        'type1-0-1':         'equals',
        'value1-0-1':        '+',
        'field1-0-2':        'cf_tracking_firefox'+str(vt.esr),
        'type1-0-2':         'equals',
        'value1-0-2':        '+',
        'include_fields':    '_all',
    }
    return options


def getToFollowUp(emails, vt):
    options = {
        'email1':           emails,
        'email1_type':      'contains_any_words',
        'email1_assigned_to':        1,
        'negate0':          1,
        'field0-0-0':       'cf_tracking_firefox'+str(vt.beta),
        'type0-0-0':        'not_equals',
        'value0-0-0':       '+',
        'field0-0-1':       'cf_status_firefox'+str(vt.beta),
        'type0-0-1':        'contains_any_words',
        'value0-0-1':       'fixed, wontfix, unaffected, verified, disabled',
        'field0-1-0':       'cf_tracking_firefox'+str(vt.beta),
        'type0-1-0':        'equals',
        'value0-1-0':       '+',
        'field0-1-1':       'cf_status_firefox'+str(vt.beta),
        'type0-1-1':        'not_equals',
        'value0-1-1':       'affected',
        'field0-2-0':       'cf_tracking_firefox'+str(vt.aurora),
        'type0-2-0':        'not_equals',
        'value0-2-0':       '+',
        'field0-2-1':       'cf_status_firefox'+str(vt.aurora),
        'type0-2-1':        'contains_any_words',
        'value0-2-1':       'fixed, wontfix, unaffected, verified, disabled',
        'field0-3-0':       'cf_tracking_firefox'+str(vt.aurora),
        'type0-3-0':        'equals',
        'value0-3-0':       '+',
        'field0-3-1':       'cf_status_firefox'+str(vt.aurora),
        'type0-3-1':        'not_equals',
        'value0-3-1':       'affected',
        'include_fields':   '_all',
    }
    return options


def getNeedsInfo(emails, vt):
    options = {
        'field0-0-0':       'cf_tracking_firefox' + str(vt.beta),
        'type0-0-0':        'contains_any_words',
        'value0-0-0':       '+,?',
        'field0-0-1':       'cf_tracking_firefox' + str(vt.aurora),
        'type0-0-1':        'contains_any_words',
        'value0-0-1':       '+,?',
        'field0-0-2':       'cf_tracking_firefox' + str(vt.esr),
        'type0-0-2':        'contains_any_words',
        'value0-0-2':       '+,?',
        'field0-1-0':       'cf_status_firefox' + str(vt.beta),
        'type0-1-0':        'not_contains_any_words',
        'value0-1-0':       'fixed, wontfix, unaffected, verified, disabled',
        'field0-1-1':       'cf_status_firefox' + str(vt.aurora),
        'type0-1-1':        'not_contains_any_words',
        'value0-1-1':       'fixed, wontfix, unaffected, verified, disabled',
        'field0-1-2':       'cf_status_firefox' + str(vt.esr),
        'type0-1-2':        'not_contains_any_words',
        'value0-1-2':       'fixed, wontfix, unaffected, verified, disabled',
        'field1-0-0':       'requestees.login_name',
        'type1-0-0':        'contains_any_words',
        'value1-0-0':       emails,
        'include_fields':   '_all',
    }
    return options


def getProdComp(product, components, vt):
    options = {
        'field0-0-0':        'status',
        'type0-0-0':         'contains_any_words',
        'value0-0-0':        'NEW, ASSIGNED, REOPENED, UNCONFIRMED',
        'field0-1-0':        'cf_tracking_firefox' + str(vt.beta),
        'type0-1-0':         'contains_any_words',
        'value0-1-0':        '+,?',
        'field0-1-1':        'cf_tracking_firefox' + str(vt.aurora),
        'type0-1-1':         'contains_any_words',
        'value0-1-1':        '+,?',
        'field0-1-2':        'cf_tracking_firefox' + str(vt.esr),
        'type0-1-2':         'contains_any_words',
        'value0-1-2':        '+,?',
        'field0-2-0':        'cf_status_firefox' + str(vt.beta),
        'type0-2-0':         'contains_any_words',
        'value0-2-0':        '---,affected',
        'field0-2-1':        'cf_status_firefox' + str(vt.aurora),
        'type0-2-1':         'contains_any_words',
        'value0-2-1':        '---,affected',
        'field0-2-2':        'cf_status_firefox' + str(vt.esr),
        'type0-2-2':         'contains_any_words',
        'value0-2-2':        '---,affected',
        'field1-0-0':        'product',
        'type1-0-0':         'contains',
        'value1-0-0':        product,
        'field2-0-0':        'component',
        'type2-0-0':         'contains_any_words',
        'value2-0-0':        components,
        'include_fields':    '_all',
    }
    return options
