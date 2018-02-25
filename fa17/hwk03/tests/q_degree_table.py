test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(np.mean(degree_data['degree']),2) 
          6.3799999999999999
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> round(np.sum(degree_data['degree'])) 
          440
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
