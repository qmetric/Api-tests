@bolt-ons-rules
Feature: All boltons rules are applied

Scenario: DirectMail referrer selection returns HEC Select (£0)
  Given the consultant submit an enquiry with "directMail" affiliate
  Then bolton "HEC Select (£0)" is preselected

Scenario: Non DirectMAIL referrer selection does not returns HEC Select (£0)
   Given the consultant submit an enquiry without "directMail" selected
   Then the bolton "HEC Select (£0) is not preselected

Scenario: HEC standard, select £(0) and select Plus £(26.95) are not available for rented main residencies, key fobs available
    Given the consultant submit an enquiry for a "rented main" residence
    Then "HEC standard, HEC select £(0), HEC select Plus £(26.95)" are not available
    And  legal and keys fobs are available

Scenario: HEC & legal standard, select £(0), select Plus £(26.95) are not available for second residencies, key fobs available
    Given the consultant submit an enquiry for a "second residence"
    Then "HEC standard, HEC select £(0), HEC select Plus £(26.95), legal standard, legal select £(0), legal select Plus £(26.95)" are not available
    And the keys fobs are available

Scenario: HEC & legal standard, select £(0), select Plus £(26.95) are not available for Rental properties, key fobs available
    Given the consultant submit an enquiry for a "Rental property"
    Then "HEC standard, HEC select £(0), HEC select Plus £(26.95), legal standard, legal select £(0), legal select Plus £(26.95)" are not available
    And the keys fobs are available

Scenario: HEC & legal standard, select £(0), select Plus £(26.95) and key fobs are not available for holiday residencies
    Given the consultant submit an enquiry for a Holiday residence
    Then "HEC standard, HEC select £(0), HEC select Plus £(26.95), legal standard, legal select £(0), legal select Plus £(26.95)" are not available
    And the keys fobs are available

Scenario: HEC & legal standard, select £(0), select Plus £(26.95) and key fobs are not available for Holiday let
   Given the consultant submit an enquiry for a Holiday let
   Then "HEC standard, HEC select £(0), HEC select Plus £(26.95), legal standard, legal select £(0), legal select Plus £(26.95), keys fobs" are not available

Scenario: HEC & legal standard, select £(0), select Plus £(26.95) and key fobs are not available for properties unoccupied for 30 days +
    Given the consultant submit an enquiry for an unoccupied residency
    Then "HEC standard, HEC select £(0), HEC select Plus £(26.95), legal standard, legal select £(0), legal select Plus £(26.95), keys fobs" are not available

