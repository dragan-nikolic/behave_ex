Feature: Restful Booking Application

  Scenario: Test get booking
    When I request Mark's bookings
    Then I should receive Mark's bookings info
 
  Scenario: Test add booking
    When I add new booking
    Then I should see new booking in the list

  @wip
  Scenario: Test update booking

  @wip
  Scenario: Test remove booking    
