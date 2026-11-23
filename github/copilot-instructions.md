# Context for Copilot

## Who we are
We're a pair of design students in HCDE 310, learning Python and Flask.

## How we work with AI (Stage 4: spec first)
- Don't write requirements or acceptance checks for us. Before writing code, ask us what the feature should do, its inputs and outputs, and 2-3 checks, then wait for our answer.
- After we provide a spec, point out any missing edge cases or unclear assumptions without silently adding scope.
- Build in small pieces. Before changing files, tell us exactly which files you expect to edit and summarize the change.
- Explain unfamiliar Python, Flask, HTML, CSS, or API concepts briefly and use terminology from class.
- Prefer readable code that helps us learn over clever abstractions or excessive frameworks.
- Do not create app code, routes, data models, UI, or dependency changes until we confirm a feature spec.
- Do not commit unless we explicitly say to commit.

## How we like to work
- Make one focused change at a time and show the relevant diff before expanding scope.
- Keep code examples and explanations concise. For each change, include what changed, why, and how to verify it.
- Use Python 3, Flask, Jinja, HTML, CSS, and JavaScript that fit a beginner-friendly small app.
- Follow existing project patterns once code exists. If no pattern exists, propose a simple approach and wait for approval.
- Use `pytest` for tests and keep acceptance checks understandable.
- Do not add packages unless they are needed for a confirmed feature and listed in `requirements.txt`.
- Do not expose API keys or secrets in source files, templates, prompts, logs, or committed documentation.

## Our project
The working direction is a small Flask web app for National Park visitors to find National Park information on campgrounds and things to do within the parks and to also check the weather conditions for their planned visit.

- Primary concept: let a user enter a US state and return a list of National parks, then be able to select a park to view its campgrounds and activities and then select dates within the next two weeks to check weather conditions for their planned visit. Alternatively, a user can enter a National Park name, return matching campgrounds and activities, and view weather conditions for their planned visit. We will be using the National Park Service API and Open Meteo API to fetch this data.
- Lens/depth: National parks, campgrounds, activities, and weather conditions for planned visits. User will be able to login and save their selections. User will also receive emails with National Park Service alerts for their saved parks.
- Core noun: `NationalPark`; its intended fields are `name`, `state`, `campgrounds`, `activities`, and `weather`.
- Persistence decision: National Park information and user selections must remain available after reload.
- User flow under consideration: search by state or park name -> review result options -> select a park -> view campgrounds and activities -> select dates -> check weather conditions.
- Planned APIs: National Park Service API and Open Meteo API. API-specific endpoints, limits, authentication, caching, and error behavior are not decided.
- Source-of-truth documents: `p1.md` contains the concept, `inclass13.md` contains the initial noun/persistence decision, and `requirements.txt` contains the current dependencies.
- There is no application code in the repository yet. Do not infer a folder structure or framework conventions beyond Flask.

## Not decided yet
-How will we save email addresses for users?
-How to send users emails about National Park Service alerts for their saved parks.
-How to store login credentials for users.
-How to have a timer check for alerts and send email notifications to users.
-How exactly to combine data from the National Park Service API and Open Meteo API for displa


## Wrap up
When we say "wrap up":
- Update `ai_use.md` with the date.
- Add one line for each file or function you wrote or changed, starting with `AI draft: check me.`.
- Leave `Reflection:` blank.
- Summarize any verification performed and any known limitations.
- Suggest a commit message.
- Do not commit unless we explicitly say yes.