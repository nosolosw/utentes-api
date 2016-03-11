# -*- coding: utf-8 -*-

import dateutil.parser


class IsNotNull():

    def fails(self, value):
        if value is None:
            return True
        return False


class IsDate():
    '''
    The received value is a valid datetime.date object or can be parsed with
    dateutil.parser. This allows strings in ISO8601 or RFC3329 or others
    '''
    def fails(self, value):
        if not value:
            return False
        try:
            dateutil.parser.parse(value)
        except:
            return True

        return False


class IsNumeric():
    '''
    The received value is the representation of a number.
    So '5' is considered valid
    '''
    def fails(self, value):
        if not value:
            return False
        try:
            float(value)
        except:
            return True
        return False


class IsBoolean():
    '''
    Value is a proper boolean.
    '''
    def fails(self, value):
        return value not in [True, False, None]


class Validator():

    def __init__(self, schemaValidateFrom):
        self.messages = []
        self.schema = schemaValidateFrom
        self.rules = {
            'NOT_NULL':   IsNotNull(),
            'IS_DATE':    IsDate(),
            'IS_NUMERIC': IsNumeric(),
            'IS_BOOLEAN': IsBoolean(),
        }

    def validate(self, model):
        self.messages = []

        for definition in self.schema:
            for rulename in definition['rules']:
                rule = self.get_rule(rulename)
                if isinstance(rule, dict):
                    model[definition['fieldname']]
                    if rule['fails'](model[definition['fieldname']]):
                        self.messages.append(definition['message'])
                else:
                    if rule.fails(model[definition['fieldname']]):
                        self.messages.append(definition['message'])

        return self.messages

    def get_rule(self, rulename):
        return self.rules[rulename]

    def add_rule(self, rulename, rule_def):
        self.rules[rulename] = rule_def
