test = {
  'name': 'Question',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> attribute_to_table(example_er, 'gender').group('gender').where('gender', are.equal_to('F')).column('count')[0]
          105
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
