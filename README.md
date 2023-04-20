# cider-documentation

This repository contains the source files for the documentation for the Cider software package. The docs are exposed [here](https://global-policy-lab.github.io/cider-documentation/intro.html). The Cider repository is [here](https://github.com/Global-Policy-Lab/cider).

To update this documentation:
* Make changes to source
* Build the changes using jupyter-book
* Delete the contents of the `docs/` folder, and then copy the contents of `_build/html/` into`docs/`.
* Create an empty file called `.nojekyll` in the `docs/` folder.
* Push your changes to your remote branch, then merge to the main branch of the repo. They should then be live within a couple of minutes. It's worth checking [the live docs](https://global-policy-lab.github.io/cider-documentation/intro.html) to make sure everything worked.