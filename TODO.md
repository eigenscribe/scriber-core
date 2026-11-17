- [ ] Update content in `/src/cli/` and `/src/frontend/` so that it exhaustively includes all functionality of 
  `../THE_SCRIBER_EXPERIENCE/cli/messaging.py`.
  - [x] Fix circular and casing import errors between `src/frontend/__init__.py` and `src/frontend/THE_SCRIBER_EXPERIENCE/cli/` modules to enable clean CLI execution.
- [ ] Remove `src/frontend/THE_SCRIBER_EXPERIENCE/cli/` folder from repo.
  - **Steps:**
    1. Update `src/cli/` and `src/frontend` folders so they include all functionality of 
       [messaging.py](@src/frontend/THE_SCRIBER_EXPERIENCE/cli/messaging.py).
    2. Remove [messaging.py](@src/frontend/THE_SCRIBER_EXPERIENCE/cli/messaging.py) from the repo.
    3. Check that all `src` files that are not contained in `../THE_SCRIBER_EXPERIENCE/cli/` all work together so that 
       their functionality exhaustively includes functionality of the files contained in 
       `../THE_SCRIBER_EXPERIENCE/cli/`.
    4. Delete `../THE_SCRIBER_EXPERIENCE/cli/` from the repository.
  - [x] Update relative import fallbacks in `src/frontend/THE_SCRIBER_EXPERIENCE/cli/main.py` and `gradients.py` to prevent partially initialized module import failures.
- [ ] Review `src/cli/` files and @src/frontend/colors.py and @src/frontend/gradients.py .
  - [ ] Consistency check.
      - [ ] Update @docs/workspace-setup-guide.md so that it keeps `COLOR_PALLETE` in `@src/frontend/colors.py` as the
        source of truth for all color variables. 
        - [ ] Things to include
          - **Constraint:** All color variables must be defined in a way that imports and uses the key names from 
            `COLOR_PALLETE` in`@src/frontend/colors.py`.
  - [ ] Create a markdown file that provides a table of all color variables and their corresponding values in 
    `@src/frontend/colors.py` and gradients defined in `@src/frontend/gradients.py` and/or any `src` files. 
  - [ ] Provide an overview of the good, the bad, and the ugly.
- [ ] Implement any changes based on consistency check.
---
- [ ] Update @README.md to match the workspace setup guide.
- [x] Update @docs/workspace-setup-guide.md and all other relevant files (e.g., @.junie/AGENTS.md) so they exhaustively
  incorporate standards and constraints from COOP blogs on cactus-style packaging and cli.
- [ ] Update repository to follow cactus-style packaging and cli.
---
- [ ] Create pypi project named `scriber-core`.
- [ ] Install `scriber-core` as a dependency in `@.junie/AGENTS.md`.
---
- [ ] Create a minimal theme generator `src` folder using best practices and includes a way to...
  - [ ] Create repo-specific color pallette and gradient generators using `@src/frontend/colors.py` and 
     `@src/frontend/gradients.py`.
  - [ ] Add preview functionality to `@src/cli`:
    - [ ] Exhaustive preview of `scriber-core` presets...
      - [x] Colors defined in `COLOR_PALLETTE` as previewable colors.
          - => Prints gradient squares OR prints table (see @src/cli/colors_table.py) of `COLOR_PALLETTE` colors.
      - [ ] Gradients defined in `@src/frontend/gradients.py` as previewable gradients.
          - => Prints gradient of squares OR prints table of colors (referenced from @src/frontend/colors.py) 
            corresponding to `GRADIENT_PRESET` gradient.
    - [ ] Exhaustive preview og repo-specific theme colors and gradients => prints a table OR prints 

  - [ ] Rename @src/cli/colors.py so it does not get confused with @src/frontend/colors.py. 
     - **Steps:**
       - Check @src/cli/colors.py for any functions that could be used in context outside of cli development. If there
         are any non-cli-specific styling functions, remove them from @src/cli/colors.py and add them to 
         @src/frontend/colors.py.
       - Check @src/frontend/colors.py for any functions that are cli-specific. Provide a list of cli-specific functions
         to user and ask which one should be moved to @src/cli/colors.py.
       - Rename @src/cli/colors.py based on changes made.
  - [ ] Remove any redundant files from `src/cli`.
  - [ ] Create a USERGUIDE.md in @src/cli that describes details on how to use `scriber-core` to create a theme.
  - [ ] Update @README.md .
- [ ] Repo-wide consistency check (regarding @docs/workspace-setup-guide.md standards/constraints). Provide a report of
  the good, the bad, and the ugly.
---
- [ ] Install `scriber-core` in `kuramoto-benchmark-suite`
  - [ ] Test cactus-style packaging and cli 
    - [ ] Try using `scriber-core` to remove 'code noise' from problem 16 
      jupyter notebook
    - [ ] Try updating `kuramoto-benchmark-suite` cli so that it implements `scriber-core/src/cli/..` and 
      @src/frontend/colors.py & @src/frontend/gradients.py personalization functionality
