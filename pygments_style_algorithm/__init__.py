# -*- coding: utf-8 -*-
"""
    pygments.styles.algorithm
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Simple print-friendly style for displaying algorithms.


    :copyright: Copyright 2012 Noah K. Tilton
    :license: BSD, same as Pygments.  See LICENSE file
    :acknowledgements: Thanks to Hugo Maia Vieira for the setuptools structure.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace


class AlgorithmStyle(Style):
    """
    Simple print-friendly style for displaying algorithms.
    """

    background_color = "#f8f8f8"
    default_style = ""

    styles = {
        Whitespace:                "#000",
        Comment:                   "noitalic #333",
        Comment.Preproc:           "noitalic #000",

        #Keyword:                   "bold #AA22FF",
        Keyword:                   "bold #000",
        Keyword.Pseudo:            "nobold",
        Keyword.Type:              "nobold #000",

        Operator:                  "#000",
        Operator.Word:             "bold #000",

        Name.Builtin:              "bold #000",
        Name.Function:             "bold #000",
        Name.Class:                "bold #0000FF",
        Name.Namespace:            "bold #0000FF",
        Name.Exception:            "bold #D2413A",
        Name.Variable:             "#19177C",
        Name.Constant:             "#880000",
        Name.Label:                "#A0A000",
        Name.Entity:               "bold #999999",
        Name.Attribute:            "#7D9029",
        Name.Tag:                  "bold #008000",
        Name.Decorator:            "#AA22FF",

        String:                    "#000",
        String.Doc:                "#333",
        String.Interpol:           "bold #BB6688",
        String.Escape:             "bold #BB6622",
        String.Regex:              "#BB6688",
        #String.Symbol:             "#B8860B",
        String.Symbol:             "bold #000",
        String.Other:              "#008000",
        Number:                    "#000",

        Generic.Heading:           "bold #000080",
        Generic.Subheading:        "bold #800080",
        Generic.Deleted:           "#A00000",
        Generic.Inserted:          "#00A000",
        Generic.Error:             "#FF0000",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold #000080",
        Generic.Output:            "#888",
        Generic.Traceback:         "#04D",

        Error:                     "border:#FF0000"
    }
