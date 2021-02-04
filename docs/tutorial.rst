Tutorial
========

.. note:: Do you find any of these instructions confusing? `Edit this file`_
          and submit a pull request with your improvements!

.. _`Edit this file`: https://github.com/romnn/cookiecutter-webgl/blob/master/docs/tutorial.rst

To start with, you will need a `GitHub account`_.
Create these before you get started on this tutorial.
If you are new to Git and GitHub, you should probably spend a few
minutes on some of the tutorials at the top of the page at `GitHub Help`_.

.. _`GitHub account`: https://github.com/
.. _`PyPI`: https://pypi.python.org/pypi
.. _`GitHub Help`: https://help.github.com/


|:cookie:| Step 1: Install Cookiecutter
---------------------------------------

Install ``cookiecutter>=1.4.0``:

.. code-block:: console

    $ pip install cookiecutter>=1.4.0


|:package:| Step 2: Generate Your Package
-----------------------------------------

Now it's time to generate your project.

Use cookiecutter, pointing it at the cookiecutter-webgl repo:

.. code-block:: console

    $ cookiecutter https://github.com/romnn/cookiecutter-webgl.git

You'll be asked to enter a bunch of values to set the package up.
If you don't know what to enter, stick with the defaults.


|:octopus:| Step 3: Create a GitHub Repo
----------------------------------------

Go to your GitHub account and create a new repo named ``myproject``,
where ``myproject`` matches the ``[project_slug]`` from your answers to running
cookiecutter.
This is so that Travis CI can find it when we get to Step 4.

You will find one folder named after the ``[project_slug]``.
Move into this folder, and then setup git to use your GitHub repo
and upload the code:

.. code-block:: console

    $ cd myproject
    $ git init .
    $ git add .
    $ git commit -m "Initial commit."
    $ git remote add origin git@github.com:myusername/myproject.git
    $ git push -u origin master

Where ``myusername`` and ``myproject`` are adjusted for your
username and project.

You can use HTTPS to push the repository,
but it's more convenient to use a ssh key to push the repo.
You can `generate`_ a key or `add`_ an existing one.

.. _`generate`: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
.. _`add`: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/

|:construction_worker:| Step 4: Set up TravisCI
-----------------------------------------------

`Travis-CI`_ [*]_ is a continuous integration tool used
to prevent integration problems.
Every commit to the master branch will trigger
automated builds of the application.

Add the repository to your Travis-CI account by activating it.
If you have connected travis with GitHub this is done automatically.

.. [*] For private projects go to `travis-ci.com`_, for public ones go to `travis-ci.org`_ has been a thing.
       But afaik all projects should use `travis-ci.com`_ as of now.

.. _`Travis-CI`: https://travis-ci.com/
.. _`travis-ci.org`: https://travis-ci.org/
.. _`travis-ci.com`: https://travis-ci.com/
.. _the installation guide: https://github.com/travis-ci/travis.rb#installation

|:pencil:| Step 5: Set up GitHub Pages
--------------------------------------

`GitHub Pages`_ is a service offered by GitHub that will host a static
website along with your project's code for free.
Per default, GitHub Pages uses `jekyll <https://jekyllrb.com/>`_
for templating, but you can use any other tool as long as it generates
static html (like ``yarn build``).
Once enabled in GitHub's repository settings, it works by hosting any
static assets (using ``index.html`` as an entrypoint) in a branch named
``gh-pages``. When using static html from another tool, GitHub requires
a file named ``.nojekyll``
in the branches root so ``jekyll`` won't be used.

If you do not want to deploy to `GitHub Pages`_,
remove the ``deploy pages`` build stage from ``.travis.yml``.

If you wish to deploy to GitHub Pages,
`generate a GitHub access token <https://github.com/settings/tokens>`_ for
`public_repo` and set this token in your travis build settings at
`<https://travis-ci.com/myusername/myproject/settings>`_ as a secret
environment variable ``GH_TOKEN``.
This will allow travis to access the secret token as ``$GH_TOKEN``
to be able to commit and push to the ``gh-pages`` branch.
The website will be available at `<https://myusername.github.io/myproject/>`_.

The default ``deploy pages`` stage in your templated project's ``.travis.yml``
will already publish your WebGL experiment to Pages,
but you might deploy a different website for your project.

.. _GitHub Pages: https://pages.github.com/

|:rotating_light:| Having problems?
-----------------------------------

If you experience problems you cannot fix by yourself, `create an issue`_.
Be sure to give as much information as possible.

.. _`create an issue`: https://github.com/audreyr/cookiecutter-webgl/issues
