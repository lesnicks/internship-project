# Created by nickles at 11/5/24
Feature: # Enter feature name here
  # Enter feature description here

   Scenario: User can search for a product
    Given Open the main page
    When Log in to the page
    And Click on settings option
    Then Click on Add a project
     And Verify the right page opens
    And Add some test information to the input fields
    Then Verify the right information is present in the input fields
    And Verify “Send an application” button is available and clickable
