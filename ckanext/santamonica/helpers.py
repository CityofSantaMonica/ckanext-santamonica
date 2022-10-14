import ckan.plugins.toolkit as toolkit


def dataset_groups():
    '''Return a list of the groups in the dataset.'''

    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    groups = toolkit.get_action('group_list')(
        data_dict={'all_fields': True})
    return groups
