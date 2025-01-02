# Edit the config_and_params.json file and add the necessary parameter values.
# Ensure that the provided input_params yield the correct output schema.
# Add logic for validating conditional_output_schema or if schema is other than dict.
# Add any specific assertions in each test case, based on the expected response.

"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import pytest
from testframework.conftest import valid_configuration, invalid_configuration, valid_configuration_with_token,\
    connector_id, connector_details, info_json, params_json, initial_setup
from testframework.helpers.test_helpers import run_health_check_success, run_invalid_config_test, run_success_test,\
    run_output_schema_validation, run_invalid_param_test, set_report_metadata
    

@pytest.mark.check_health
def test_check_health_success(valid_configuration, connector_details):
    set_report_metadata(connector_details, "Health Check", "Verify with valid Configuration")
    result = run_health_check_success(valid_configuration, connector_details)
    assert result.get('status').lower() == 'available'
    

@pytest.mark.check_health
def test_check_health_invalid_server_url(invalid_configuration, connector_id, connector_details, params_json):
    set_report_metadata(connector_details, "Health Check", "Verify with invalid Server URL")
    result = run_invalid_config_test(invalid_configuration, connector_id, connector_details, param_name='server_url',
                                     param_type='text', config=params_json['config'])
    assert result.get('status').lower() == "disconnected"
    

@pytest.mark.check_health
def test_check_health_invalid_token(invalid_configuration, connector_id, connector_details, params_json):
    set_report_metadata(connector_details, "Health Check", "Verify with invalid API Token/Bearer Token")
    result = run_invalid_config_test(invalid_configuration, connector_id, connector_details, param_name='token',
                                     param_type='password', config=params_json['config'])
    assert result.get('status').lower() == "disconnected"
    

@pytest.mark.check_health
def test_check_health_invalid_username(invalid_configuration, connector_id, connector_details, params_json):
    set_report_metadata(connector_details, "Health Check", "Verify with invalid Username")
    result = run_invalid_config_test(invalid_configuration, connector_id, connector_details, param_name='username',
                                     param_type='text', config=params_json['config'])
    assert result.get('status').lower() == "disconnected"
    

@pytest.mark.create_ticket
def test_create_ticket_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Create Ticket", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='create_ticket',
                                   action_params=params_json['create_ticket']):
        assert result.get('status') == "Success"


@pytest.mark.create_ticket
def test_validate_create_ticket_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Create Ticket", "Validate Output Schema")
    run_output_schema_validation(cache, 'create_ticket', info_json, params_json['create_ticket'])
    

@pytest.mark.create_ticket
def test_create_ticket_invalid_priority(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Create Ticket", "Verify with invalid Priority")
    result = run_invalid_param_test(connector_details, operation_name='create_ticket', param_name='priority',
                                    param_type='text', action_params=params_json['create_ticket'])
    assert result.get('status') == "failed"
    

@pytest.mark.create_ticket
def test_create_ticket_invalid_other_fields(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Create Ticket", "Verify with invalid Other Fields")
    result = run_invalid_param_test(connector_details, operation_name='create_ticket', param_name='other_fields',
                                    param_type='json', action_params=params_json['create_ticket'])
    assert result.get('status') == "failed"
    

@pytest.mark.create_ticket
def test_create_ticket_invalid_parent(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Create Ticket", "Verify with invalid Parent Key ID")
    result = run_invalid_param_test(connector_details, operation_name='create_ticket', param_name='parent',
                                    param_type='text', action_params=params_json['create_ticket'])
    assert result.get('status') == "failed"
    

@pytest.mark.create_ticket
def test_create_ticket_invalid_issue_type(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Create Ticket", "Verify with invalid Ticket Type")
    result = run_invalid_param_test(connector_details, operation_name='create_ticket', param_name='issue_type',
                                    param_type='text', action_params=params_json['create_ticket'])
    assert result.get('status') == "failed"
    
    

@pytest.mark.create_ticket
def test_create_ticket_invalid_project_key(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Create Ticket", "Verify with invalid Project Key")
    result = run_invalid_param_test(connector_details, operation_name='create_ticket', param_name='project_key',
                                    param_type='text', action_params=params_json['create_ticket'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_ticket_details
def test_get_ticket_details_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ticket Details", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_ticket_details',
                                   action_params=params_json['get_ticket_details']):
        assert result.get('status') == "Success"


@pytest.mark.get_ticket_details
def test_validate_get_ticket_details_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Ticket Details", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_ticket_details', info_json, params_json['get_ticket_details'])
    

@pytest.mark.get_ticket_details
def test_get_ticket_details_invalid_issue_key(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Ticket Details", "Verify with invalid Ticket ID")
    result = run_invalid_param_test(connector_details, operation_name='get_ticket_details', param_name='issue_key',
                                    param_type='text', action_params=params_json['get_ticket_details'])
    assert result.get('status') == "failed"
    

@pytest.mark.list_projects
def test_list_projects_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "List Projects", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='list_projects',
                                   action_params=params_json['list_projects']):
        assert result.get('status') == "Success"


@pytest.mark.list_projects
def test_validate_list_projects_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "List Projects", "Validate Output Schema")
    run_output_schema_validation(cache, 'list_projects', info_json, params_json['list_projects'])
    

@pytest.mark.list_tickets
def test_list_tickets_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "List Tickets", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='list_tickets',
                                   action_params=params_json['list_tickets']):
        assert result.get('status') == "Success"


@pytest.mark.list_tickets
def test_validate_list_tickets_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "List Tickets", "Validate Output Schema")
    run_output_schema_validation(cache, 'list_tickets', info_json, params_json['list_tickets'])
    

@pytest.mark.list_tickets
def test_list_tickets_invalid_jql_query(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "List Tickets", "Verify with invalid JQL Query")
    result = run_invalid_param_test(connector_details, operation_name='list_tickets', param_name='jql_query',
                                    param_type='text', action_params=params_json['list_tickets'])
    assert result.get('status') == "failed"
    

@pytest.mark.fetch_tickets
def test_fetch_tickets_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Fetch Tickets", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='fetch_tickets',
                                   action_params=params_json['fetch_tickets']):
        assert result.get('status') == "Success"


@pytest.mark.fetch_tickets
def test_validate_fetch_tickets_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Fetch Tickets", "Validate Output Schema")
    run_output_schema_validation(cache, 'fetch_tickets', info_json, params_json['fetch_tickets'])
    

@pytest.mark.fetch_tickets
def test_fetch_tickets_invalid_jql_query(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Fetch Tickets", "Verify with invalid JQL Query")
    result = run_invalid_param_test(connector_details, operation_name='fetch_tickets', param_name='jql_query',
                                    param_type='text', action_params=params_json['fetch_tickets'])
    assert result.get('status') == "failed"
    

@pytest.mark.fetch_tickets
def test_fetch_tickets_invalid_maxresults(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Fetch Tickets", "Verify with invalid Max Results")
    result = run_invalid_param_test(connector_details, operation_name='fetch_tickets', param_name='maxResults',
                                    param_type='integer', action_params=params_json['fetch_tickets'])
    assert result.get('status') == "failed"
    
    

@pytest.mark.fetch_tickets
def test_fetch_tickets_invalid_nextpagetoken(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Fetch Tickets", "Verify with invalid Next Page Token")
    result = run_invalid_param_test(connector_details, operation_name='fetch_tickets', param_name='nextPageToken',
                                    param_type='text', action_params=params_json['fetch_tickets'])
    assert result.get('status') == "failed"
    

@pytest.mark.validate_jql_query
def test_validate_jql_query_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Validate JQL query", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='validate_jql_query',
                                   action_params=params_json['validate_jql_query']):
        assert result.get('status') == "Success"


@pytest.mark.validate_jql_query
def test_validate_validate_jql_query_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Validate JQL query", "Validate Output Schema")
    run_output_schema_validation(cache, 'validate_jql_query', info_json, params_json['validate_jql_query'])

    

@pytest.mark.search_users
def test_search_users_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Search Users", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='search_users',
                                   action_params=params_json['search_users']):
        assert result.get('status') == "Success"


@pytest.mark.search_users
def test_validate_search_users_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Search Users", "Validate Output Schema")
    run_output_schema_validation(cache, 'search_users', info_json, params_json['search_users'])
    

@pytest.mark.search_users
def test_search_users_invalid_maxresults(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Search Users", "Verify with invalid Max Results")
    result = run_invalid_param_test(connector_details, operation_name='search_users', param_name='maxResults',
                                    param_type='integer', action_params=params_json['search_users'])
    assert result.get('status') == "failed"
    

@pytest.mark.search_users
def test_search_users_invalid_startat(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Search Users", "Verify with invalid Start At")
    result = run_invalid_param_test(connector_details, operation_name='search_users', param_name='startAt',
                                    param_type='integer', action_params=params_json['search_users'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_user_details
def test_get_user_details_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get User Details", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_user_details',
                                   action_params=params_json['get_user_details']):
        assert result.get('status') == "Success"


@pytest.mark.get_user_details
def test_validate_get_user_details_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get User Details", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_user_details', info_json, params_json['get_user_details'])
    

@pytest.mark.get_user_details
def test_get_user_details_invalid_accountid(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get User Details", "Verify with invalid Account ID")
    result = run_invalid_param_test(connector_details, operation_name='get_user_details', param_name='accountId',
                                    param_type='text', action_params=params_json['get_user_details'])
    assert result.get('status') == "failed"
    

@pytest.mark.assign_issue
def test_assign_issue_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Assign Issue to User", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='assign_issue',
                                   action_params=params_json['assign_issue']):
        assert result.get('status') == "Success"


@pytest.mark.assign_issue
def test_validate_assign_issue_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Assign Issue to User", "Validate Output Schema")
    run_output_schema_validation(cache, 'assign_issue', info_json, params_json['assign_issue'])
    

@pytest.mark.assign_issue
def test_assign_issue_invalid_accountid(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Assign Issue to User", "Verify with invalid Account ID")
    result = run_invalid_param_test(connector_details, operation_name='assign_issue', param_name='accountId',
                                    param_type='text', action_params=params_json['assign_issue'])
    assert result.get('status') == "failed"
    

@pytest.mark.assign_issue
def test_assign_issue_invalid_issue_key(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Assign Issue to User", "Verify with invalid Ticket ID")
    result = run_invalid_param_test(connector_details, operation_name='assign_issue', param_name='issue_key',
                                    param_type='text', action_params=params_json['assign_issue'])
    assert result.get('status') == "failed"
    

@pytest.mark.submit_file
def test_submit_file_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Add Attachment", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='submit_file',
                                   action_params=params_json['submit_file']):
        assert result.get('status') == "Success"


@pytest.mark.submit_file
def test_validate_submit_file_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Add Attachment", "Validate Output Schema")
    run_output_schema_validation(cache, 'submit_file', info_json, params_json['submit_file'])
    

@pytest.mark.submit_file
def test_submit_file_invalid_issue_key(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Add Attachment", "Verify with invalid Ticket ID")
    result = run_invalid_param_test(connector_details, operation_name='submit_file', param_name='issue_key',
                                    param_type='text', action_params=params_json['submit_file'])
    assert result.get('status') == "failed"
    

@pytest.mark.submit_file
def test_submit_file_invalid_value(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Add Attachment", "Verify with invalid Attachment ID")
    result = run_invalid_param_test(connector_details, operation_name='submit_file', param_name='value',
                                    param_type='text', action_params=params_json['submit_file'])
    assert result.get('status') == "failed"
    

@pytest.mark.add_remote_link
def test_add_remote_link_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Add Remote Link", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='add_remote_link',
                                   action_params=params_json['add_remote_link']):
        assert result.get('status') == "Success"


@pytest.mark.add_remote_link
def test_validate_add_remote_link_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Add Remote Link", "Validate Output Schema")
    run_output_schema_validation(cache, 'add_remote_link', info_json, params_json['add_remote_link'])
    
    

@pytest.mark.add_remote_link
def test_add_remote_link_invalid_issue_key(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Add Remote Link", "Verify with invalid Ticket ID")
    result = run_invalid_param_test(connector_details, operation_name='add_remote_link', param_name='issue_key',
                                    param_type='text', action_params=params_json['add_remote_link'])
    assert result.get('status') == "failed"
    

@pytest.mark.add_remote_link
def test_add_remote_link_invalid_url(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Add Remote Link", "Verify with invalid URL")
    result = run_invalid_param_test(connector_details, operation_name='add_remote_link', param_name='url',
                                    param_type='text', action_params=params_json['add_remote_link'])
    assert result.get('status') == "failed"
    

@pytest.mark.add_comment
def test_add_comment_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Add Comment", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='add_comment',
                                   action_params=params_json['add_comment']):
        assert result.get('status') == "Success"


@pytest.mark.add_comment
def test_validate_add_comment_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Add Comment", "Validate Output Schema")
    run_output_schema_validation(cache, 'add_comment', info_json, params_json['add_comment'])
    

@pytest.mark.add_comment
def test_add_comment_invalid_issue_key(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Add Comment", "Verify with invalid Ticket ID")
    result = run_invalid_param_test(connector_details, operation_name='add_comment', param_name='issue_key',
                                    param_type='text', action_params=params_json['add_comment'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_comments
def test_get_comments_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Comments", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_comments',
                                   action_params=params_json['get_comments']):
        assert result.get('status') == "Success"


@pytest.mark.get_comments
def test_validate_get_comments_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Comments", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_comments', info_json, params_json['get_comments'])
    

@pytest.mark.get_comments
def test_get_comments_invalid_issue_key(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Comments", "Verify with invalid Ticket ID")
    result = run_invalid_param_test(connector_details, operation_name='get_comments', param_name='issue_key',
                                    param_type='text', action_params=params_json['get_comments'])
    assert result.get('status') == "failed"
    

@pytest.mark.set_status
def test_set_status_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Set Ticket Status", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='set_status',
                                   action_params=params_json['set_status']):
        assert result.get('status') == "Success"


@pytest.mark.set_status
def test_validate_set_status_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Set Ticket Status", "Validate Output Schema")
    run_output_schema_validation(cache, 'set_status', info_json, params_json['set_status'])
    

@pytest.mark.set_status
def test_set_status_invalid_issue_key(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Set Ticket Status", "Verify with invalid Ticket ID")
    result = run_invalid_param_test(connector_details, operation_name='set_status', param_name='issue_key',
                                    param_type='text', action_params=params_json['set_status'])
    assert result.get('status') == "failed"
    

@pytest.mark.set_status
def test_set_status_invalid_status(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Set Ticket Status", "Verify with invalid Status")
    result = run_invalid_param_test(connector_details, operation_name='set_status', param_name='status',
                                    param_type='text', action_params=params_json['set_status'])
    assert result.get('status') == "failed"
    

@pytest.mark.update_ticket
def test_update_ticket_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update Ticket", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='update_ticket',
                                   action_params=params_json['update_ticket']):
        assert result.get('status') == "Success"


@pytest.mark.update_ticket
def test_validate_update_ticket_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Update Ticket", "Validate Output Schema")
    run_output_schema_validation(cache, 'update_ticket', info_json, params_json['update_ticket'])
    

@pytest.mark.update_ticket
def test_update_ticket_invalid_priority(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update Ticket", "Verify with invalid Priority")
    result = run_invalid_param_test(connector_details, operation_name='update_ticket', param_name='priority',
                                    param_type='text', action_params=params_json['update_ticket'])
    assert result.get('status') == "failed"
    

@pytest.mark.update_ticket
def test_update_ticket_invalid_issue_key(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update Ticket", "Verify with invalid Ticket ID")
    result = run_invalid_param_test(connector_details, operation_name='update_ticket', param_name='issue_key',
                                    param_type='text', action_params=params_json['update_ticket'])
    assert result.get('status') == "failed"
    

@pytest.mark.update_ticket
def test_update_ticket_invalid_other_fields(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update Ticket", "Verify with invalid Other Fields")
    result = run_invalid_param_test(connector_details, operation_name='update_ticket', param_name='other_fields',
                                    param_type='json', action_params=params_json['update_ticket'])
    assert result.get('status') == "failed"
    

@pytest.mark.update_ticket
def test_update_ticket_invalid_status(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update Ticket", "Verify with invalid Status")
    result = run_invalid_param_test(connector_details, operation_name='update_ticket', param_name='status',
                                    param_type='text', action_params=params_json['update_ticket'])
    assert result.get('status') == "failed"
    


@pytest.mark.update_fortisoar
def test_validate_update_fortisoar_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Update FortiSOAR Record", "Validate Output Schema")
    run_output_schema_validation(cache, 'update_fortisoar', info_json, params_json['update_fortisoar'])
    

@pytest.mark.update_fortisoar
def test_update_fortisoar_invalid_cyops_password(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update FortiSOAR Record", "Verify with invalid FortiSOAR Password")
    result = run_invalid_param_test(connector_details, operation_name='update_fortisoar', param_name='cyops_password',
                                    param_type='text', action_params=params_json['update_fortisoar'])
    assert result.get('status') == "failed"
    

@pytest.mark.update_fortisoar
def test_update_fortisoar_invalid_jira_key(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update FortiSOAR Record", "Verify with invalid Ticket ID")
    result = run_invalid_param_test(connector_details, operation_name='update_fortisoar', param_name='jira_key',
                                    param_type='text', action_params=params_json['update_fortisoar'])
    assert result.get('status') == "failed"
    

@pytest.mark.update_fortisoar
def test_update_fortisoar_invalid_cyops_username(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update FortiSOAR Record", "Verify with invalid FortiSOAR Username")
    result = run_invalid_param_test(connector_details, operation_name='update_fortisoar', param_name='cyops_username',
                                    param_type='text', action_params=params_json['update_fortisoar'])
    assert result.get('status') == "failed"
    

@pytest.mark.delete_ticket
def test_delete_ticket_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Delete Ticket", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='delete_ticket',
                                   action_params=params_json['delete_ticket']):
        assert result.get('status') == "Success"


@pytest.mark.delete_ticket
def test_validate_delete_ticket_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Delete Ticket", "Validate Output Schema")
    run_output_schema_validation(cache, 'delete_ticket', info_json, params_json['delete_ticket'])
    

@pytest.mark.delete_ticket
def test_delete_ticket_invalid_issue_key(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Delete Ticket", "Verify with invalid Ticket ID")
    result = run_invalid_param_test(connector_details, operation_name='delete_ticket', param_name='issue_key',
                                    param_type='text', action_params=params_json['delete_ticket'])
    assert result.get('status') == "failed"
    
