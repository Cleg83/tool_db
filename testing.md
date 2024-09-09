![Screenshot of The Woodworker's Tool DB on several screen sizes](tool_db/static/images/am-i-res.png)

# Detailed Manual Testing for the Woodworker's Tool Database

<br>

# Non-registered users

## Navbar

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Logo | Redirects user to home page | Clicked logo | User redirected to home page | Pass |
| Home link | Redirects user to home page | Clicked link | User redirected to home page | Pass |
| Categories link | Redirects user to categories page | Clicked link | User redirected to categories page | Pass |
| Glossary link | Redirects user to glossary page | Clicked link | User redirected to glossary page | Pass |
| Log in link | Redirects user to log in page | Clicked link | User redirected to log in page | Pass |

## Home page

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Home page tool card | Random tool card changes every 10 seconds | Waited on page for 1 minute to see if card changes the correct amount of times | Card changed every 10 seconds | Pass |
Tool name link in tool card | Redirects user to selected tool page | Clicked link | User redirected to selected tool page | Pass |

## Categories page

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Main Category Text & Icon Link | Redirects user to selected main category page | Clicked link | User redirected to correct selected category page | Pass |
| Show Subcategory Text & Icon | Reveals card content with list of related subcategories | Clicked link | Correct card content revealed | Pass |
| Subcategory links in revealed card content  | Redirects user to selected subcategory | Clicked all subcategory links | User redirected to correct selected subcategory page | Pass |
| Go To Main Category link | User redirected to selected main category page | Clicked link | User redirected to correct selected category page | Pass |

## Glossary page

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Tool link | Redirects user to selected tool page | Clicked link | User redirected to correct selected tool page | Pass |
| Tool Description Summary link | Expands summary to reveal hidden tool description | Clicked summary link | Summary expands to show tool description | Pass |

## Log In Page
Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Username input field | Allows user to input text | Input text | User allowed to input text | Pass |
| Username input field | Field marked red if requirements not met | Input text that did not meet requirements | Field marked red | Pass |
| Password input field | Allows user to input text | Input text | User allowed to input text | Pass |
| Password input field | Field marked red if requirements not met | Input text that did not meet requirements | Field marked red | Pass |
| Login button | Alerts user to requirements not being met if user input doesn't meet requirements | Clicked button with requirements not met | User alerted to the requirements not being met and username not updated | Pass | 
| Login button | Does not allow users to login if they enter incorrect login details | Clicked button after inputting incorrect login details | Message displays advising that the login attempt failed and user redirected to login page | Pass | 
| Login button | Logs user into site, message displays advising that the user is logged in and user redirected to home page | Clicked button | User logged in, correct message displayed and user redirected to home page |
| Cancel link | Redirects user to home page | Clicked Link | User redirected to home page | Pass |
| Register link | Redirects user to register page | Clicked Link | User redirected to register page | Pass |

## Register Page
Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Username input field | Allows user to input text | Input text | User allowed to input text | Pass |
| Username input field | Field marked red if requirements not met | Input text that did not meet requirements | Field marked red | Pass |
| Password input field | Allows user to input text | Input text | User allowed to input text | Pass |
| Password input field | Field marked red if requirements not met | Input text that did not meet requirements | Field marked red | Pass |
| Confirm password input field | Allows user to input text | Input text | User allowed to input text | Pass |
| Confirm password input field | Field marked red if requirements not met | Input text that did not meet requirements | Field marked red | Pass |
| Register button | Alerts user to requirements not being met if user input doesn't meet requirements | Clicked button with requirements not met | User alerted to the requirements not being met and username not updated | Pass | 
| Register button | Does not allow users to register if they enter mismatching passwords details | Clicked button after inputting mismatching password details | User alerted to passwords not matching and is not allowed to register | Pass | 
| Register button | Registers profile, message displays advising that the user profile has been created and user redirected to log in page | Clicked button | Profile registered, correct message displays and user redirected to log in page |
| Cancel link | Redirects user to home page | Clicked Link | User redirected to home page | Pass |
| Log In link | Redirects user to log in page | Clicked Link | User redirected to log in page | Pass |

## Footer 

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Footer Home link | Redirects user to home page | Clicked link | User redirected to home page | Pass |
| Footer Categories link | Redirects user to categories page | Clicked link | User redirected to categories page | Pass |
| Footer Glossary link | Redirects user to glossary page | Clicked link | User redirected to glossary page | Pass |
| Footer Log in link | Redirects user to log in page | Clicked link | User redirected to log in page | Pass |

<br>

# Registered users (logged in)

## Navbar

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Home page loads on successful log in | Home page loads on successful log in | Logged in | Home page loaded on successful log in | Pass |
| Logo | Redirects user to home page | Clicked logo | User redirected to home page | Pass |
| Home link | Redirects user to home page | Clicked link | User redirected to home page | Pass |
| Categories link | Redirects user to categories page | Clicked link | User redirected to categories page | Pass |
| Glossary link | Redirects user to glossary page | Clicked link | User redirected to glossary page | Pass |
| My Toolbox link | Redirects user to my toolbox page | Clicked link | User redirected to my toolbox page | Pass |
| Profile | Redirects user to profile page | Clicked link | User redirected to profile page | Pass |
| Log Out link | Logs user out and displays flash message | Clicked link | User logged out and flash message displayed | Pass |

## Home page

## Categories page

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Main Category Text & Icon Link | Redirects user to selected main category page | Clicked link | User redirected to correct selected category page | Pass |
| Show Subcategory Text & Icon | Reveals card content with list of related subcategories | Clicked link | Correct card content revealed | Pass |
| Subcategory links in revealed card content  | Redirects user to selected subcategory | Clicked all subcategory links | User redirected to correct selected subcategory page | Pass |
| Go To Main Category link | User redirected to selected main category page | Clicked link | User redirected to correct selected category page | Pass |

## Glossary Page

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Tool name link | Redirects user to selected tool page | Clicked link | User redirected to correct tool page | Pass |
| Tool Description Summary link | Expands summary to reveal hidden tool description | Clicked summary link | Summary expands to show tool description | Pass |
| Add to my toolbox link | Adds tool to users toolbox, redirects user to my toolbox page and correct flash message is shown | Clicked link to add tool | Tool added to user's toolbox, redirected to my toolbox page and correct flash message displayed | Pass | 


## My Toolbox page

This is the same for admin and logged in non-admin users.

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Tool name link | Redirects user to selected tool page | Clicked link | User redirected to correct tool page | Pass |
| Tool product links | Opens link in new browser tab | Clicked link | Product link opens in new tab | Pass |
| Tool Video links | Opens link in new browser tab | Clicked link | Video link opens in new tab | Pass |
| Remove button | Removes tool from toolbox, confirmation message displays and user is redirected to my toolbox | Clicked button | Tool removed from toolbox, correct flash message displayed and user is redirected to my toolbox page| Pass |

## Profile Page

This is the same for admin and logged in non-admin users.

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Change Username Button | Redirects user to change username page | Clicked button | User redirected to change username page | Pass |
| Change Password Button | Redirects user to change password page | Clicked button | User redirected to change password page | Pass |
| Delete Profile button  | Displays confirm delete modal | Clicked button | Confirm delete modal displayed | Pass |
| Modal Cancel button | Closes modal | Clicked button | Modal closed | Pass |
| Modal Delete button | Deletes profile, redirects user to home page and displays flash message | Clicked button | Profile deleted, user redirected to categories page and correct flash message displayed | Pass |

## Edit Username

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Username input filed on page load | Input field pre-populated with current username | Loaded page | Input field populated with correct username | Pass | 
| Username input field | Allows user to input text | Input text | User allowed to input text | Pass |
| Username input field | Field marked red if requirements not met | Input text that did not meet requirements | Field marked red | Pass |
| Update button | Alerts user to requirements not being met if user input doesn't meet requirements | Clicked button with requirements not met | User alerted to the requirements not being met and username not updated | Pass | 
| Update button | Updates username, message displays advising username has been updated and user redirected to profile page | Clicked button | Username updated, correct message displayed and user redirected to profile page |
| Cancel link | Redirects user to profile page | Clicked Link | User redirected to home page | Pass |

## Edit Password

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| New password input field | Allows user to input text | Input text | User allowed to input text | Pass |
| New password input field | Field marked red if requirements not met | Input text that did not meet requirements | Field marked red | Pass |
| Confirm password input field | Allows user to input text | Input text | User allowed to input text | Pass |
| Confirm password input field | Field marked red if requirements not met | Input text that did not meet requirements | Field marked red | Pass |
| Update button | Alerts user to requirements not being met if user input doesn't meet requirements | Clicked button with requirements not met | User alerted to the requirements not being met and username not updated | Pass | 
| Update button | Does not allow user to submit if passwords do not match | Clicked button with mismatching passwords | User alerted to the fact that passwords do not match and was not allowed to proceed | Pass | 
| Update button | Does not allow user to submit if either input field is left blank | Clicked button with one or the other input field left blank | User not allowed to update password | Pass | 
| Update button | Updates password, message displays advising password has been updated and user redirected to profile page | Clicked button | Password updated, correct message displayed and user redirected to profile page |
| Cancel link | Redirects user to profile page | Clicked Link | User redirected to home page | Pass |

## Footer

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Footer Home link | Redirects user to home page | Clicked link | User redirected to home page | Pass |
| Footer Categories link | Redirects user to categories page | Clicked link | User redirected to categories page | Pass |
| Footer Glossary link | Redirects user to glossary page | Clicked link | User redirected to glossary page | Pass |
| Footer My Toolbox link | Redirects user to my toolbox page | Clicked link | User redirected to my toolbox page | Pass |
| Footer Profile | Redirects user to profile page | Clicked link | User redirected to profile page | Pass |
| Footer Log Out link | Logs user out and displays flash message | Clicked link | User logged out and flash message displayed | Pass |

<br> 

#  Admin User (logged in)

## Navbar

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Categories link shows active on successful login | Categories link shows as active on successful log in | Logged in as admin | Categories link displayed as active on successful log in | Pass |
| Logo | Redirects user to home page | Clicked logo | User redirected to home page | Pass |
| Home link | Redirects user to home page | Clicked link | User redirected to home page | Pass |
| Categories link | Redirects user to categories page | Clicked link | User redirected to categories page | Pass |
| Glossary link | Redirects user to glossary page | Clicked link | User redirected to glossary page | Pass |
| My Toolbox link | Redirects user to my toolbox page | Clicked link | User redirected to my toolbox page | Pass |
| Profile link | Redirects user to profile page | Clicked link | User redirected to profile page | Pass |
| Add Category link | Redirects user to add category page | Clicked link | User redirected to add category page | Pass |
| Add Category link | Redirects user to add category page | Clicked link | User redirected to add category page | Pass |
| Add Tool link | Redirects user to add tool page | Clicked link | User redirected to add tool page | Pass |
| Manage Users link | Redirects user to manage users page | Clicked link | User redirected to manage users page | Pass |
| Log Out link | Logs user out and displays flash message | Clicked link | User logged out and flash message displayed | Pass |

## Categories page

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Main Category Text & Icon Link | Redirects user to selected main category page | Clicked link | User redirected to correct selected category page | Pass |
| Show Subcategory Text & Icon | Reveals card content with list of related subcategories + edit & delete buttons | Clicked link | Correct card content revealed | Pass |
| Subcategory links in revealed card content  | Redirects user to selected subcategory | Clicked all subcategory links | User redirected to correct selected subcategory page | Pass |
| Edit Subcategory button  | Redirects user to correct edit subcategory page | Clicked button | User redirected to correct edit subcategory page | Pass |
| Delete Subcategory button  | Displays confirm delete modal | Clicked button | Confirm delete modal displayed | Pass |
| Add Subcategory button  | Redirects user to add subcategory page | Clicked button | User redirected to add subcategory page | Pass |
| Modal Cancel button | Closes modal | Clicked button | Modal closed | Pass |
| Modal Delete button | Deletes subcategory, redirects user to categories page and displays flash message | Clicked button | Subcategory deleted, user redirected to categories page and correct flash message displayed | Pass |
| Go To Main Category link | User redirected to selected main category page | Clicked link | User redirected to correct selected category page | Pass |
| Edit Main Category button | Redirects user to correct edit main category page | Clicked button | User redirected to correct edit main category page | Pass | 
| Delete Main Category button  | Displays confirm delete modal | Clicked button | Confirm delete modal displayed | Pass |
| Modal Cancel button | Closes modal | Clicked button | Modal closed | Pass |
| Modal Delete button | Deletes main category, redirects user to categories page and displays flash message | Clicked button | Main category deleted, user redirected to categories page and correct flash message displayed | Pass |
| Add category card icon link | redirects user to add category page | Clicked icon | User redirected to add main category page | Pass |

## Glossary Page

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Tool name link | Redirects user to selected tool page | Clicked link | User redirected to correct selected tool page | Pass |
| Tool Description Summary link | Expands summary to reveal hidden tool description | Clicked summary link | Summary expands to show tool description | Pass |
| Edit tool link | Redirects user to correct edit tool page | Clicked link | User redirected to correct selected tool page | Pass | 
| Add to my toolbox link | Adds tool to users toolbox, redirects user to my toolbox page and correct flash message is shown | Clicked link to add tool | Tool added to user's toolbox, redirected to my toolbox page and correct flash message displayed | Pass | 

## Add Category page

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Add main category button | Redirects user to add main category page | Clicked button | User redirected to add main category page | Pass |
| Add subcategory button | Redirects user to add subcategory page | Clicked button | User redirected to add subcategory page | Pass |

## Add Main Category

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Main category input field | Allows user to input text | Input text | User able to input text | Pass | 
| Main category input field | Alerts user if requirements are not met | Input text but that does not match requirements | User alerted to requirements not being met | Pass | 
| Add Category button | Adds category to database, displays confirmation message and redirect user to categories page | Clicked button | Category added to db, correct confirmation message displayed and user redirected to categories page | Pass |
| Add Category button | Does not allow user to add category if input field left blank or does not meet requirements | Clicked button | User not allowed to add tool if field left blank or requirements not met | Pass |
| Cancel link | Redirects user to home page | Clicked Link | User redirected to home page | Pass |

## Add Subcategory

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Subcategory input field | Allows user to input text | Input text | User able to input text | Pass | 
| Subcategory input field | Alerts user if requirements are not met | Input text but that does not match requirements | User alerted to requirements not being met | Pass | 
| Choose main category dropdown | Displays the list of main categories when expanded | Expanded dropdown | All main categories listed and selectable | Pass |
| Add Subcategory button | Adds subcategory to database, displays confirmation message and redirect user to categories page | Clicked button | Subcategory added to db, correct confirmation message displayed and user redirected to categories page | Pass |
| Add Subcategory button | Does not allow user to add category if input field left blank or does not meet requirements and if no main category is selected | Clicked button | User not allowed to add tool if field left blank, requirements not met or main category not selected | Pass |
| Cancel link | Redirects user to home page | Clicked Link | User redirected to home page | Pass |

## Add Tool page

### Step 1

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Tool name input field | Only allows text input between 5 & 50 characters (allowing spaces) | Input text to meet the specified criteria | Input field marked green for requirements met | Pass |
| Tool name input field | Does not allow field to be left blank | Clicked into next input field after selecting but not inputting any text | Tool name input field marked red for requirements not met | Pass |
| Tool name input field | Does not allow only spaces to be entered | Clicked into next input field after inputting 5 spaces | Tool name input field marked red for requirements not met | Pass |
| Tool description input field | Only allows text input between 5 & 1500 characters (allowing spaces) | Input text to meet the specified criteria | Input field marked green for requirements met | Pass |
| Tool description input field | Does not allow field to be left blank | Clicked into next input field after selecting but not inputting any text | Tool name input field marked red for requirements not met | Pass |
| Tool description input field | Does not allow only spaces to be entered | Clicked into next input field after inputting 5 spaces | Tool name input field marked red for requirements not met | Pass |
| Video link input field & next button | Only allows text input between 5 & 5000 characters (allowing commas & spaces), in the specified format | Input text to meet the specified criteria and moved to next step | User redirected to next step| Pass |
| Video link input field & next button | Does not allow field to be left blank | Clicked into next input field after selecting but not inputting any text | Tool name input field marked red for requirements not met | Pass |
| Product link input field & next button | Only allows text input between 5 & 5000 characters (allowing commas & spaces), in the specified format | Input text to meet the specified criteria and moved to next step | User redirected to next step| Pass |
| Product link input field & next button | Does not allow field to be left blank | Clicked into next input field after selecting but not inputting any text | Tool name input field marked red for requirements not met | Pass |
| Next button | Will not allow user to progress if form requirements are not met | Clicked button with requirements not met | USer alerted to requirements not being met and user not allowed to progress | Pass | 
| Next button | Allows user to progress if form requirements met | Clicked button with requirements met | User redirected to add tool step 2 | Pass | 
| Cancel link | Redirects user to home page | Clicked Link | User redirected to home page | Pass |

### Step 2

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Choose main category dropdown | Displays the list of main categories when expanded | Expanded dropdown | All main categories listed and selectable | Pass |
| Next button | Does not allow user to progress if no main category is selected | Clicked button | User not allowed to progress if no main category is selected | Pass |
| Next button | Allows user to progress if main category selected from dropdown | Clicked button | User redirected to add tool step 3 | Pass |
| Cancel link | Redirects user add main category page | Clicked Link | User redirected to add main category page | Pass |

### Step 3

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Choose subcategory dropdown | Displays the list of subcategories when expanded | Expanded dropdown | All subcategories listed and selectable | Pass |
| Add tool button | Does not allow user to progress if no subcategory is selected | Clicked button | User not allowed to progress if no subcategory is selected | Pass |
| Add tool button | Tool added to database, message displays advising tool has been added and user redirected to categories | Clicked button | Tool added to db, correct message displayed and user redirected to categories | Pass |
| Cancel link | Redirects user add subcategory page | Clicked Link | User redirected to add main category page | Pass |

## Manage Users page

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Delete user button | Displays confirm delete modal | Clicked button | Confirm delete modal displayed | Pass |
| Modal Cancel button | Closes modal | Clicked button | Modal closed | Pass |
| Modal Delete button | Deletes selected user, redirects user to manage users page and displays flash message | Clicked button | Selected user deleted, user redirected to manage users page and correct flash message displayed | Pass |

## Add Category page

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Add main category button | Redirects user to add main category page | Clicked button | User redirected to add main category page | Pass |
| Add subcategory button | Redirects user to add subcategory page | Clicked button | User redirected to add subcategory page | Pass |

## Edit Main Category

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Category name field on page load | Input field pre-populated with current main category | Loaded page | Input field pre-populated with correct main category | Pass | 
| Category name input field | Allows user to input text | Input text | User able to input text | Pass | 
| Category name input field | Alerts user if requirements are not met | Input text but that does not match requirements | User alerted to requirements not being met | Pass | 
| Save Changes button | Saves changes to database, displays confirmation message and redirect user to categories page | Clicked button | DB entry updated, correct confirmation message displayed and user redirected to categories page | Pass |
| Save Changes button | Does not allow user to add category if input field left blank or does not meet requirements | Clicked button | User not allowed to add tool if field left blank or requirements not met | Pass |
| Cancel link | Redirects user to categories page | Clicked Link | User redirected to home page | Pass |

## Edit Subcategory

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Subcategory name input field on page load | Input field pre-populated with current subcategory | Loaded page | Input field pre-populated with correct main category | Pass |
| Subcategory name field | Allows user to input text | Input text | User able to input text | Pass | 
| Subcategory name field | Alerts user if requirements are not met | Input text but that does not match requirements | User alerted to requirements not being met | Pass | 
| Choose main category dropdown on page load | Input field pre-populated with current main category | Loaded page | Input field pre-populated with correct main category | Pass | 
| Choose main category dropdown | Displays the list of main categories when expanded | Expanded dropdown | All main categories listed and selectable | Pass |
| Save Changes button | Adds subcategory to database, displays confirmation message and redirect user to categories page | Clicked button | Subcategory added to db, correct confirmation message displayed and user redirected to categories page | Pass |
| Save Changes button | Does not allow user to add category if input field left blank or does not meet requirements and if no main category is selected | Clicked button | User not allowed to add tool if field left blank, requirements not met or main category not selected | Pass |
| Cancel link | Redirects user to categories page | Clicked Link | User redirected to home page | Pass |

## Edit Tool

### Step 1

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| On page load | All input fields are pre-populated with tool data | Loaded page | Input fields correctly populated with tool data | Pass | 
| Tool name input field | Only allows text input between 5 & 50 characters (allowing spaces) | Input text to meet the specified criteria | Input field marked green for requirements met | Pass |
| Tool name input field | Does not allow field to be left blank | Clicked into next input field after selecting but not inputting any text | Tool name input field marked red for requirements not met | Pass |
| Tool name input field | Does not allow only spaces to be entered | Clicked into next input field after inputting 5 spaces | Tool name input field marked red for requirements not met | Pass |
| Tool description input field | Only allows text input between 5 & 1500 characters (allowing spaces) | Input text to meet the specified criteria | Input field marked green for requirements met | Pass |
| Tool description input field | Does not allow field to be left blank | Clicked into next input field after selecting but not inputting any text | Tool name input field marked red for requirements not met | Pass |
| Tool description input field | Does not allow only spaces to be entered | Clicked into next input field after inputting 5 spaces | Tool name input field marked red for requirements not met | Pass |
| Video link input field & next button | Only allows text input between 5 & 5000 characters (allowing commas & spaces), in the specified format | Input text to meet the specified criteria and moved to next step | User redirected to next step| Pass |
| Video link input field & next button | Does not allow field to be left blank | Clicked into next input field after selecting but not inputting any text | Tool name input field marked red for requirements not met | Pass |
| Product link input field & next button | Only allows text input between 5 & 5000 characters (allowing commas & spaces), in the specified format | Input text to meet the specified criteria and moved to next step | User redirected to next step| Pass |
| Product link input field & next button | Does not allow field to be left blank | Clicked into next input field after selecting but not inputting any text | Tool name input field marked red for requirements not met | Pass |
| Next button | Will not allow user to progress if form requirements are not met | Clicked button with requirements not met | USer alerted to requirements not being met and user not allowed to progress | Pass | 
| Next button | Allows user to progress if form requirements met | Clicked button with requirements met | User redirected to add tool step 2 | Pass | 
| Cancel link | Redirects user to home page | Clicked Link | User redirected to home page | Pass |

### Step 2

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| On page load | Main category dropdown pre-populated with correct main category | Loaded page | Dropdown populated with correct main category | Pass | 
| Choose main category dropdown | Displays the list of main categories when expanded | Expanded dropdown | All main categories listed and selectable | Pass |
| Next button | Does not allow user to progress if no main category is selected | Clicked button | User not allowed to progress if no main category is selected | Pass |
| Next button | Allows user to progress if main category selected from dropdown | Clicked button | User redirected to add tool step 3 | Pass |
| Cancel link | Redirects user add main category page | Clicked Link | User redirected to add main category page | Pass |

### Step 3

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| On page load | Subcategory dropdown pre-populated with correct subcategory | Loaded page | Dropdown populated with correct subcategory | Pass | 
| Choose subcategory dropdown | Displays the list of subcategories for the main category selected in step 2 when expanded | Expanded dropdown | All associated subcategories listed and selectable | Pass |
| Save changes button | Does not allow user to progress if no subcategory is selected | Clicked button | User not allowed to progress if no subcategory is selected | Pass |
| Save changes button | Saves changes to db, message displays advising tool has been updated and user redirected to edit subcategory page | Clicked button | Changes saved, correct message displayed and user redirected to edit subcategories page | Pass |
| Cancel link | Redirects user add subcategory page | Clicked Link | User redirected to add main category page | Pass |

## Footer

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
Footer Home link | Redirects user to home page | Clicked link | User redirected to home page | Pass |
| Categories link | Redirects user to categories page | Clicked link | User redirected to categories page | Pass |
| Footer Glossary link | Redirects user to glossary page | Clicked link | User redirected to glossary page | Pass |
| Footer My Toolbox link | Redirects user to my toolbox page | Clicked link | User redirected to my toolbox page | Pass |
| Footer Profile link | Redirects user to profile page | Clicked link | User redirected to profile page | Pass |
| Footer Add Category link | Redirects user to add category page | Clicked link | User redirected to add category page | Pass |
| Footer Add Tool link | Redirects user to add tool page | Clicked link | User redirected to add tool page | Pass |
| Footer Manage Users link | Redirects user to manage users page | Clicked link | User redirected to manage users page | Pass |
| Footer Log Out link | Logs user out and displays flash message | Clicked link | User logged out and flash message displayed | Pass |