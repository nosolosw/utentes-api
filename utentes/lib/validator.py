# -*- coding: utf-8 -*-


class IsNotNull():

    def fails(self, value):
        if value is None:
            return True
        return False


class Validator():

    def __init__(self, schemaValidateFrom):
        self.messages = []
        self.schema = schemaValidateFrom
        self.rules = {
            'NOT_NULL': IsNotNull()
        }

    def validate(self, model):
        self.messages = []

        for definition in self.schema:
            for rulename in definition['rules']:
                rule = self.get_rule(rulename)
                print rule
                if isinstance(rule, dict):
                    print model
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
