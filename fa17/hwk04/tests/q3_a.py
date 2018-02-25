test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.mean(er_res.column(0)) > 0.029
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(np.corrcoef(er_res['cc'], er_res['apl'])[0,1], 1) == -0.2
          True
          """,
          'hidden': False,
          'locked': False
        }                
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}