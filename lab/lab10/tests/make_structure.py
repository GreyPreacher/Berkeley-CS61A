test = {
  'name': 'make-list',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define a '(1))
          a
          scm> a
          (1)
          scm> (define b (cons 2 a))
          b
          scm> b
          (2 1)
          scm> (define c (list 3 b))
          c
          scm> c
          4473b526bf89266454bf0d18a3167b0b
          # locked
          scm> (car c)
          154ae95398009673bcf6847be0496a27
          # locked
          scm> (cdr c)
          4c117c29d319c285b6a835d9bb6093f7
          # locked
          scm> (car (car (cdr c)))
          8f01429f05539100445ff1214be81240
          # locked
          scm> (cdr (car (cdr c)))
          2c988a84918e0b2958168830ef8b7391
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> lst ; type out exactly how Scheme would print the list that will be defined in this problem (see spec)
          d27fa7ae58e6e5c9334663d5f70ed8d8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
