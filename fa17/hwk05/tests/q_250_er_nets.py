test = {
  'name': 'Question',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> str(np.abs(np.round(np.mean(er_r[0]), 2)))
          '0.0'
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> str(np.abs(np.round(np.mean(er_r[1]), 2)))
          '0.0'
          """,
          'hidden': False
        },                
      ],
            
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
