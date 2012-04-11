Install
=======

Github
------

::

    % git clone git://github.com/noah/pygments-style-algorithm.git
    % cd pygments-style-algorithm
    # python setup.py install


Usage example
=============

::

    >>> from pygments.formatters import HtmlFormatter
    >>> HtmlFormatter(style='algorithm').style
    <class 'pygments_style_algorithm.AlgorithmStyle'>


Using in LaTeX documents
========================

::
    \usepackage{minted}
    \usemintedstyle{algorithm}



Pygments styles available
-----------------------

To get a list of all available styles, execute the following command on
the command line::

    $ pygmentize -L styles

Please read the `official documentation`_ for further information on the usage
of pygment styles.

.. _official documentation: http://pygments.org/docs/


Acknowledgement
------

This structure of this package is based on pygments-style-github by Hugo Maia Vieira 

.. _pygments-style-github: https://github.com/hugomaiavieira/pygments-style-github
