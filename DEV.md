# Development

This is my first real package. To develop this package, first clone it:

    git clone https://github.com/ccorcos/se3.git

Then to symlink it to your python path, run:

    sudo python setup.py develop

This way you can actively develop the package.

The package was registered with PyPI with (don't forget your username and password in your `~/.pypirc`):

    python setup.py register

The package is uploaded with

    python setup.py sdist upload

When you are done developing, you can uninstall with:

    sudo python setup.py develop --uninstall

# Rst, Markdown, Html

I like writing things with markdown. I have created some scripts to convert to rst and html files with mathjax, etc. Check them out: `md2rst` and `md2html`
