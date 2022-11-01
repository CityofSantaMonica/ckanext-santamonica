import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.plugins import DefaultTranslation

from ckanext.santamonica import helpers


class SantamonicaPlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.ITranslation)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets',
                             'santamonica')
        toolkit.add_resource('fanstatic',
                             'santamonica')

    def get_helpers(self):
        '''Register the dataset_groups function above as a template
        helper function.
        '''
        return {
            'santamonica_dataset_orgs': helpers.dataset_orgs,
        }
