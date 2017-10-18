test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(avg_path_length(add_health_networks[3]), 3) == 3.364
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(avg_path_length(add_health_networks[1]), 3) == 3.194
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