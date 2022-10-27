import ckan.plugins.toolkit as toolkit


def dataset_orgs():
    '''Return a list of the orgs in the data portal.'''

    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    orgs = toolkit.get_action('organization_list')(
        data_dict={'all_fields': True})
    return orgs
