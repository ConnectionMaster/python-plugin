import jsonpickle
import logging


class UpdateInventoryResult(object):
    def __init__(self, organization, updated_projects, created_projects, org_token):
        self.organization = organization
        self.createdProjects = created_projects
        self.updatedProjects = updated_projects
        self.orgToken = org_token


def json_to_update_inventory(json):
    """ Converts json result from server into a UpdateInventoryResult"""

    try:
        json_dict = jsonpickle.decode(json.decode("utf-8"))
        update_inventory = UpdateInventoryResult(json_dict['organization'], json_dict['updatedProjects'],
                                                 json_dict['createdProjects'], json_dict['requestToken'])
        logging.debug("The UpdateInventoryResult instance is ready")
        return update_inventory
    except Exception as err:
        logging.debug(json)
        logging.debug("Unable to parse json to UpdateInventoryResult object", err.message)
        raise




