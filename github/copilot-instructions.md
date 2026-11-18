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
The working direction is a small Flask web app for parents who want to cook an adult-friendly and a kid-friendly version of the same recipe, reducing the need to prepare separate meals.

- Primary concept: let a user enter a main ingredient, return matching recipe options, compare an adult and simplified kid-friendly version, and view recipe details.
- Lens/depth: recipes, kid-friendly adaptations, instructions, nutrition, and cost information.
- Core noun: `Recipe`; its intended fields are `title`, `original_version`, `kid_version`, and `nutrition`.
- Persistence decision: recipes saved by a user must remain available after reload.
- User flow under consideration: search by main ingredient -> review result options -> compare versions -> select a recipe -> save it with a heart-style control.
- Planned APIs: TheMealDB and Spoonacular. API-specific endpoints, limits, authentication, caching, and error behavior are not decided.
- Source-of-truth documents: `p1.md` contains the concept, `inclass13.md` contains the initial noun/persistence decision, and `requirements.txt` contains the current dependencies.
- There is no application code in the repository yet. Do not infer a folder structure or framework conventions beyond Flask.

## Not decided yet
- Which concept to implement, if the team does not confirm Concept 1.
- Which API is the primary source and whether both APIs are needed.
- Spoonacular API key availability, usage limits, and the exact fields we can retrieve.
- Whether signup/login is required or saving will initially use a simpler browser/server persistence mechanism.
- How adult and kid-friendly recipes should be generated or adapted: API data, app transformation rules, or AI-assisted text.
- The exact recipe data model, routes, template structure, save behavior, and testing setup.
- Desktop/mobile layout details, visual design, cost calculation, and nutrition display.
- How we should handle API failures, empty searches, invalid ingredients, loading states, and rate limits.

## Wrap up
When we say "wrap up":
- Update `ai_use.md` with the date.
- Add one line for each file or function you wrote or changed, starting with `AI draft: check me.`.
- Leave `Reflection:` blank.
- Summarize any verification performed and any known limitations.
- Suggest a commit message.
- Do not commit unless we explicitly say yes.