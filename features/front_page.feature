Feature: Front Page
    I want a meaningful landing page that displays the company name and has links to other pages within the site.

    Scenario: I navigate to company website
        Given I am on the landing page
        Then I see the company name
        Then I see the text "Welcome to Note Weaver!"
        Then I see a link to "https://github.com/DataByne/uraPointOfSale"
        And I see a link to "https://www.kent.edu/cs"

    Scenario: From front page I can navigate to other pages
        Given I am on the landing page
        Then I see the navigation bar
        And I can navigate to other pages

    Scenario: I see company logo
        Given I am on the landing page
        Then I see the image company logo

    Scenario: I can visit the about page
        Given I am on the about page
        Then I can see the text "About Us"
