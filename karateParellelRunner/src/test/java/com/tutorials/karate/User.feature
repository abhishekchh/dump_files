Feature: Test Single User API
  
  Scenario: Fetch single users
    Given url 'https://reqres.in/api/users/2'
    When method GET
    Then status 200
	And match $.data contains {id:2}
	And match $.data contains {email:"janet.weaver@reqres.in"}
	And match $.data contains {first_name:"Janet"}
	
	Scenario: Fetch single users
    Given url 'https://reqres.in/api/users/3'
    When method GET
    Then status 200
	And match $.data contains {id:3}
	And match $.data contains {email:"emma.wong@reqres.in"}
	And match $.data contains {first_name:"Emma"}