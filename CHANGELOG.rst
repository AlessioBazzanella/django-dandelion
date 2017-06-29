.. :changelog:

.. _KeepAChangelog: http://keepachangelog.com/
.. _SemanticVersioning: http://semver.org/

Change Log
----------

All notable changes to this project will be documented in this file.

The format is based on KeepAChangelog_ and this project adheres to SemanticVersioning_.


[0.1.4] - 2017-06-29
++++++++++++++++++++

Added
~~~~~
* Added ``top_entities`` and ``epsilon`` params to ``EntityExtraction``
* Added ``nex.top_entities`` and ``nex.epsilon`` params to ``TextSimilarity``
* Added ``nex.top_entities``, ``nex.min_confidence``, ``nex.min_length``, ``nex.social.hashtag``, ``nex.social.mention``, ``nex.include``,
``nex.extra_types``, ``nex.country``, ``nex.custom_spots`` and ``nex.epsilon`` params to ``TextSimilarity``


[0.1.3] - 2017-03-14
++++++++++++++++++++

Fixed
~~~~~
* Merge extra_dict with params in BaseDandelionParamsRequest._do_request
* Fixed app name in documentation to add to ``INSTALLED_APPS``


[0.1.2] - 2017-03-10
++++++++++++++++++++

Added
~~~~~
* User-defined spots (EntityExtraction.UserDefinedSpots())


[0.1.1] - 2017-03-10
++++++++++++++++++++

Fixed
~~~~~
* PyPI version release


[0.1.0] - 2017-03-10
++++++++++++++++++++

* First release on PyPI.
