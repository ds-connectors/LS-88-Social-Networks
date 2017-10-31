test = {
  'name': 'Question',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.sum(attribute_to_table(official_congress_twitter, 'party').group('party').column('count'))
          519
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> np.sum(attribute_to_table(official_congress_twitter, 'party').group('party').where('party', are.equal_to('Republican')).column('count'))
          291
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> np.sum(attribute_to_table(official_congress_twitter, 'party').group('party').where('party', are.equal_to('Independent')).column('count'))
          2
          """,
          'hidden': False
        },                
        {
          'code': r"""
          >>> attribute_to_table(official_congress_twitter, 'party').where('node_id', are.equal_to(402719755)).column('party')[0]
          'Democrat'
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
