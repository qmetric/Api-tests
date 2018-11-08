# file:features/policy_expert_affiliates.feature
@affiliates
Feature: Policy expert affiliate selection returns Policy expert quotes only


Scenario: Quidco affiliates returns Policy Expert quotes
  Given the consultant submit an enquiry with "Quidco" affiliate
  Then all offered quotes are "Policy Expert"

Scenario: DirectMail affiliate quotes boltons are filtered
  Given the consultant submit an enquiry with "Direct Mail" affiliate
  Then some bolt-ons are offered
  | Bolt-ons       | Price | Available | selected |
  | Legal Standard | free  | false     |  false   |
  | Legal Select   | na    | false     |  false   |
  | HEC Standard   | na    | false     |  false   |
  | Legal Plus     | 26.95 | true      |  false   |
  | HEC Plus       | 69.95 | true      |  false   |
  | keys           | na    | true      |  false   |
  | Legal Select   | free  | true      |  true    |
  | HEC Select     | free  | true      |  true    |

