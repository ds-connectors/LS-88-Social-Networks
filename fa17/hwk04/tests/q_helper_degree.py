test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(average_degree(add_health_networks[3]), 4)
          8.0854
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(average_degree(add_health_networks[30]), 4)
          4.3888
          """,
          'hidden': False,
          'locked': False
        },                
                      
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}