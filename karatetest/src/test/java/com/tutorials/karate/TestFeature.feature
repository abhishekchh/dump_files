Feature: Test User API
  Scenario: Fetch all users
    Given url 'https://reqres.in/api/users?page=2'
    When method GET
    Then status 200
#    And assert response.length == 2
#    And match response[0].name == 'FirstUser'
	And match $ contains {page:2,per_page:3,total_pages:4}
	And match $.data[0] contains {id:4,email:"eve.holt@reqres.in"}