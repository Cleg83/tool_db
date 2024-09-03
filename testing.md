# Detailed Manual Testing for the Woodworker's Tool Database

# Front End

## Non-registered users

### Default Navbar

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Logo | Redirects user to home page | Clicked logo | User redirected to home page | Pass |
| Home link | Redirects user to home page | Clicked link | User redirected to home page | Pass |
| Categories link | Redirects user to categories page | Clicked link | User redirected to categories page | Pass |
| Glossary link | Redirects user to glossary page | Clicked link | User redirected to glossary page | Pass |
| Log in link | Redirects user to log in page | Clicked link | User redirected to log in page | Pass |

### Default Home page

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |

### Default Categories page

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |

| Main Category Text & Icon Link | Redirects user to selected main category page | Clicked link | User redirected to correct selected category page | Pass |
| Show Subcategory Text & Icon | Reveals card content with list of related subcategories | Clicked link | Correct card content revealed | Pass |
| Subcategory links in revealed card content  | Redirects user to selected subcategory | Clicked all subcategory links | User redirected to correct selected subcategory page | Pass |
| Go To Main Category link | User redirected to selected main category page | Clicked link | User redirected to correct selected category page | Pass |


### Default Glossary page

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |

Tool link | Redirects user to selected tool page | Clicked link | User redirected to correct selected tool page | Pass |



## Registered users (logged in)

### User Navbar

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Home page loads on successful log in | Home page loads on successful log in | Logged in | Home page loaded on successful log in | Pass |
| Logo | Redirects user to home page | Clicked logo | User redirected to home page | Pass |
| Home link | Redirects user to home page | Clicked link | User redirected to home page | Pass |
| Categories link | Redirects user to categories page | Clicked link | User redirected to categories page | Pass |
| Glossary link | Redirects user to glossary page | Clicked link | User redirected to glossary page | Pass |
| My Toolbox link | Redirects user to my toolbox page | Clicked link | User redirected to my toolbox page | Pass |
| My Toolbox link | Redirects user to my toolbox page | Clicked link | User redirected to my toolbox page | Pass |
| Log Out link | Logs user out and displays flash message | Clicked link | User logged out and flash message displayed | Pass |

### User Home page

### User Categories page

| Main Category Text & Icon Link | Redirects user to selected main category page | Clicked link | User redirected to correct selected category page | Pass |
| Show Subcategory Text & Icon | Reveals card content with list of related subcategories | Clicked link | Correct card content revealed | Pass |
| Subcategory links in revealed card content  | Redirects user to selected subcategory | Clicked all subcategory links | User redirected to correct selected subcategory page | Pass |
| Go To Main Category link | User redirected to selected main category page | Clicked link | User redirected to correct selected category page | Pass |

### User Glossary Page



### My Toolbox page





##  Admin User (logged in)

### Admin Navbar

Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Categories page loads on successful log in | Categories page loads on successful log in | Logged in as admin | Categories page loaded on successful log in | Pass |
| Logo | Redirects user to home page | Clicked logo | User redirected to home page | Pass |
| Home link | Redirects user to home page | Clicked link | User redirected to home page | Pass |
| Categories link | Redirects user to categories page | Clicked link | User redirected to categories page | Pass |
| Glossary link | Redirects user to glossary page | Clicked link | User redirected to glossary page | Pass |
| My Toolbox link | Redirects user to my toolbox page | Clicked link | User redirected to my toolbox page | Pass |
| My Toolbox link | Redirects user to my toolbox page | Clicked link | User redirected to my toolbox page | Pass |
| Log Out link | Logs user out and displays flash message | Clicked link | User logged out and flash message displayed | Pass |

### Admin Home page

### Admin Categories page

| Main Category Text & Icon Link | Redirects user to selected main category page | Clicked link | User redirected to correct selected category page | Pass |
| Show Subcategory Text & Icon | Reveals card content with list of related subcategories + edit & delete buttons | Clicked link | Correct card content revealed | Pass |
| Subcategory links in revealed card content  | Redirects user to selected subcategory | Clicked all subcategory links | User redirected to correct selected subcategory page | Pass |
| Edit Subcategory button  | Redirects user to correct edit subcategory page | Clicked button | User redirected to correct edit subcategory page | Pass |
| Delete Subcategory button  | Displays confirm delete modal | Clicked button | Confirm delete modal displayed | Pass |
| Modal Cancel button | Closes modal | Clicked button | Modal closed | Pass |
| Modal Delete button | Deletes subcategory, redirects user to categories page and displays flash message | Clicked button | Subcategory deleted, user redirected to categories page and correct flash message displayed | Pass |
| Go To Main Category link | User redirected to selected main category page | Clicked link | User redirected to correct selected category page | Pass |
| Edit Main Category button | Redirects user to correct edit main category page | Clicked button | User redirected to correct edit main category page | Pass | 
| Delete Main Category button  | Displays confirm delete modal | Clicked button | Confirm delete modal displayed | Pass |
| Modal Cancel button | Closes modal | Clicked button | Modal closed | Pass |
| Modal Delete button | Deletes main category, redirects user to categories page and displays flash message | Clicked button | Main category deleted, user redirected to categories page and correct flash message displayed | Pass |
| Add category card icon link | redirects user to add category page | Clicked icon | User redirected to add main category page | Pass

### Admin Glossary Page

### Add Category page

### Add Tool page

### Manage Users page


# Back End