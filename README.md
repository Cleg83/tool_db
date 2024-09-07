### The Woodworker's Tool Database is an incredible new resource for woodworkers featuring a comprehensive tool glossary the ability for registered users to save their favourite tools and videos!

Visit the deployed site [here](https://tool-db-72501f8e2b40.herokuapp.com/)

- - -

## CONTENTS

* [Rationale](#rationale)
  * [Project Introduction](#project-introduction)
  * [Motivation and Inspiration](#motivation-and-inspiration)
  * [Background Information](#background-information)
  * [Project Scope and Limitations](#project-scope-and-limitations)
    * [Scope](#scope)
    * [Limitations](#limitations)
  * [Problem Statement](#problem-statement)
  * [Proposed Solution](#proposed-solution)
  * [Benefits and Advantages](#benefits-and-advantages)
  * [Future Versions](#future-versions)
  * [Summary](#summary)

* [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Wireframes](#wireframes)
    * [Desktop](#desktop)
    * [Tablet](#tablet)
    * [Mobile](#mobile)

* [Database Schema](#database-schema)
  * [ERD Diagram](#erd-diagram)
  * [Models](#models)
    * [MainCategory](#maincategory)
    * [SubCategory](#subcategory)
    * [Tool](#tool)
    * [MyToolbox](#mytoolbox)

* [Features](#features)
  * [Favicon](#favicon)
  * [Navbar](#navbar)
  * [Footer](#footer)
  * [Home Page](#home-page)
  * [Categories](#categories)
  * [Tools](#tools)
  * [Glossary](#glossary) 
* [Registered User Features](#registered-user-features)
  * [My Toolbox](#my-toolbox)
  * [Profile](#profile)
    * [Edit Profile](#edit-profile)
    * [Delete Profile](#delete-profile)
  * [Admin Features](#admin-user)
    * [Admin Navbar](#admin-navbar)
    * [Admin Categories](#admin-categories)
    * [Add Main Category](#add-main-category)
    * [Edit Main Category](#edit-main-category)
    * [Delete Main Category](#delete-main-category)
    * [Add Sub Category](#add-sub-category)
    * [Edit Sub Category](#edit-sub-category)
    * [Delete Sub Category](#delete-sub-category)
    * [Add Tool](#add-tool)
    * [Edit Tool](#edit-tool)
    * [Delete Tool](#delete-tool)
    * [Delete User](#delete-user)

* [Accessibility](#accessibility)

* [Technologies](#technologies)
  * [Languages](#languages)
  * [Frameworks, Libraries and Programs](#frameworks-libraries-and-programs)

* [Deployment and Development](#deployment-and-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [Extensions required](#extensions-required)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)
  * [Manual Testing](#manual-testing)
  * [Automated Testing](#automated-testing)
    * [W3C](#W3C)
    * [Lighthouse](#lighthouse)
    * [JS-Hint](#js-hint)
  * [Bugs](#Bugs)
  
* [Credits](#credits)

- - 

<br>

# Rationale

## Project Introduction

The Woodworking Tool Database is a comprehensive web application designed to serve woodworking enthusiasts and hobbyists by providing a centralised platform for discovering, learning about, and purchasing woodworking tools. 

The application features an extensive tool database, product videos, product links, and user-specific tool management, creating a one-stop resource for both novice and experienced woodworkers alike.

## Motivation and Inspiration

As a passionate hobbyist woodworker, the motivation behind this project stems from a desire to streamline the process of researching and purchasing woodworking tools. Previously, finding detailed information, instructional videos, and purchasing options for tools required navigating multiple sources, which was both time-consuming and inefficient. 

The inspiration for this project was to create a single, integrated resource that simplifies and enhances the tool acquisition process, thereby saving time and improving the overall woodworking experience.

## Background Information

To build anything out of wood, from the smallest bandsaw box to a monolithic cabinet; tools are essential. However, the process of selecting and purchasing the right tool often involves extensive research across multiple platforms. Users typically need to search for tool specifications, watch instructional videos, and find reliable purchase links; all of which are scattered across different websites. This fragmentation can lead to frustration and also creates a disjointed experience for users.

## Project Scope and Limitations

### Scope:

* Tool Database: A comprehensive collection of woodworking tools, each with detailed descriptions, instructional videos, and purchase links.

* User Management: Allows users to add tools to their personal toolbox and manage their profile / log in details.

* Integration: Seamlessly integrates video content and purchase options within the tool profiles.

### Limitations:

* Tool Information: The accuracy and comprehensiveness of tool data are dependent on available sources and user contributions.

* Video and Link Sources: Limited to available resources and may not cover all tools or have the latest product links.

* User Authentication: Currently supports basic authentication and may not include advanced user management features.

* Search functionality: Currently there is no way for a site user to search for tools. 

### Problem Statement

Woodworking enthusiasts face challenges in efficiently finding comprehensive information about tools, including their usage, instructional content, and purchase options. The existing fragmented resources often require users to navigate multiple websites, leading to a cumbersome and time-consuming experience. There is a need for a centralised platform that integrates tool information, instructional videos, and purchase links into a single, accessible resource.

## Proposed Solution

The Woodworking Tool Database addresses these challenges by providing an integrated web application where users can:

* Access detailed information about a wide range of woodworking tools.

* Watch instructional videos directly linked to each tool.

* Find and compare purchase options from various online retailers.

* Manage personal tool collections through a user-friendly interface.

* By consolidating these resources into one platform, the project enhances the user experience, simplifies the tool research process, and supports informed decision-making.

## Benefits and Advantages

* Centralized Resource: Combines tool information, videos, and purchase links into a single platform, saving time and effort.

* Enhanced Learning: Provides educational videos for each tool, helping users understand and utilize them more effectively.

* Convenience: Offers direct purchase links, allowing users to easily compare options and make purchases without navigating multiple websites.

* Personalization: Enables users to manage their own toolbox, keeping track of their favorite tools and preferences.


## Future Versions

Future versions of the project may include:

* Advanced User Management: Enhanced features for user profiles, tool recommendations, community interactions, password management. 

* Search and Navigation: Incorporate a search bar to search for tools by name.

* Tool Reviews and Ratings: User-generated reviews and ratings for tools to provide additional insights and feedback.

* Mobile Optimization: Improved user experience on mobile devices, including a dedicated mobile app.

* Expanded Database: Regular updates to the tool database with new tools, videos, and purchase links.

* Email integration.


## Summary

The Woodworking Tool Database is designed to simplify the process of discovering, learning about, and acquiring woodworking tools. By integrating detailed tool information, instructional videos, and purchase options into a single platform, the application addresses the fragmentation and inefficiencies in the current process. 

With its focus on user convenience and enhanced learning, the application aims to become a valuable resource for all woodworking enthusiasts.

<br>

# Design

## Color Scheme

![color scheme](tool_db/static/images/tool-db-color-scheme.png)

I wanted an elegant teal for the navbar and footer. White text in the navbar, black text in the footer. A darker teal makes an appearance in headings and the home page tool names. 

Salmon pink was chosen as it complements the teal pleasantly and is less abrasive for flash messages than a harsh red. This was also used as the hover color for most buttons.

Other than that: Dark grey for certain borders and all form buttons.

<br>

# Features

## Favicon

![favicon in browser](tool_db/static/images/favicon2.png)

The favicon is a very simple, shortened version of the app name in the same teal colour that proliferates the app.

![favicon large](tool_db/static/images/favicon.png)

<br>

## Navbar

When a visitor to the site first lands on the page, the only four items in the navbar are: 

* Home
* Categories
* Glossary
* Log In

![default navbar](tool_db/static/images/default-navbar.png)

If a user logs in, the navbar and sidenav also display the features only available to registered users:

* My Toolbox
* Profile

![user navbar](tool_db/static/images/user-navbar.png)

![user sidenav](tool_db/static/images/user-sidenav.png)

<br>

## Home Page

The Home Page for displays a random tool card that changes every ten seconds. The card contains the tool name (which is a clickable link to the tool's page) and the tool description.

![default home page](tool_db/static/images/default-home.png)

By clicking on the tool name link, the user is redirected to that tool's page which contains the name, description, product links and videos for that tool.

For users who log in, they have the additional option of adding the tool to their toolbox (more on that shortly):

![ home page](tool_db/static/images/user-home-page.png)

<br>

## Categories

![default category page](tool_db/static/images/default-categories-page.png)

The categories page for contains Materialize's handy cards for each main category and when the user clicks "show subcategories", there is a card reveal that displays the subcategories for that main category. 

![default category page, expanded card](tool_db/static/images/default-categories-expanded.png)

From here, users can navigate to the selected main category page:

![selected main category page](tool_db/static/images/selected-category.png)

 or each individual subcategory page:

 ![selected subcategory page](tool_db/static/images/selected-subcategory.png)

<br>

## Tools

Each tool has a page containing the name and description, as well as product links and videos (if present):

 ![selected tool page](tool_db/static/images/default-selected-tool-page.png)



### Glossary

The glossary page is an A-Z of all tools in the database (shown here in a rather bare state) and is the same for registered and non-registered users:

![glossary page](tool_db/static/images/default-glossary-page.png)

The tool name is a link to that tool's page and the description summary can be clicked to expand the tool description.


# Admin User

## Admin Navbar

![admin navbar](tool_db/static/images/admin-navbar.png)

The navbar for the admin user allows for easy adding of categories and tools. N.B. This functionality can be found in various places for the admin user but it seemed logical to include a direct route to these functions from the navbar (and the sidenav on smaller screens):

![admin navbar](tool_db/static/images/admin-sidenav.png)

The admin navbar does not contain the logo as it was too cluttered, the home link is still available in the navbar and footer so no functionality is lost as a result of this (and one would hope that the admin user knows how to navigate the site).

## Admin Categories

The category view for the admin user is similar to the view for non-admin users but also incorporates the functionality to edit and delete the main category.

![admin categories](tool_db/static/images/admin-categories.png)

There is also an additional card that shows after all category cards that will redirect to the add main category page when clicked (it is quite obvious as it is a smaller car with a folder-plus icon):

![Add main category card](tool_db/static/images/add-main-category-card.png)

When expanded, the admin user has the ability to edit and delete subcategories associated with that main category:

![admin categories expanded](tool_db/static/images/admin-categories-expanded.png)

### Add Main Category

Adding a main category is pretty straightforward and only requires the user to type a category name. 

![add main category](tool_db/static/images/add-main-category.png)

No other functionality or input fields were required as subcategories can be moved to different main categories when editing subcategories so this page is kept very simple indeed.

### Edit Main Category

This is pretty much identical to adding a main category with the exception of the input field being pre-populated with the current main category name.

![edit main category](tool_db/static/images/edit-main-category.png)

### Delete Main Category

Deleting a main category is done via a modal confirming if the user wishes to delete the category or cancel.

![delete main category modal](tool_db/static/images/delete-main-category.png)

And if the user chooses to delete the category, they are redirected to the categories page and a flash message is displayed.

![delete main category confirmation](tool_db/static/images/delete-main-category-confirmation.png)












### Add Subcategory

Adding a subcategory is also straightforward; the user is given two input fields to complete, 1 for the subcategory name and a dropdown to select a main category. 

![add subcategory](tool_db/static/images/add-subcategory.png)

# Testing


## Automated Testing

### Lighthouse 

Lighthouse scares for each of the many pages are all in the 90s

![lighthouse add tool](tool_db/static/images/lighthouse-add-tool.png)
![lighthouse add tool](tool_db/static/images/lighthouse-categories.png)
![lighthouse add tool](tool_db/static/images/lighthouse-glossary.png)
![lighthouse add tool](tool_db/static/images/lighthouse-home.png)
![lighthouse add tool](tool_db/static/images/lighthouse-home2.png)
![lighthouse add tool](tool_db/static/images/lighthouse-home3.png)
![lighthouse add tool](tool_db/static/images/lighthouse-manage-users.png)
![lighthouse add tool](tool_db/static/images/lighthouse-my-toolbox.png)
![lighthouse add tool](tool_db/static/images/lighthouse-profile.png)
![lighthouse add tool](tool_db/static/images/lighthouse-selected-category.png)
![lighthouse add tool](tool_db/static/images/lighthouse-selected-subcategory.png)
