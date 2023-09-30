from unittest.mock import patch, MagicMock
from app.Backend import Backend

@patch('app.requests')
def test_url_exists_with_valid_url(mock_requests):
    backend = Backend()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.head.return_value = mock_response
    url = "https://d3047k2vzxu60t.cloudfront.net/projects/project_name/key"
    result = backend.url_exists(url)
    assert result is True
    mock_requests.head.assert_called_once_with(url)

@patch('app.requests')
def test_url_exists_with_invalid_url(mock_requests):
    backend = Backend()
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_requests.head.return_value = mock_response
    url = "https://d3047k2vzxu60t.cloudfront.net/projects/project_name/key"
    result = backend.url_exists(url)
    assert result is False
    mock_requests.head.assert_called_once_with(url)

def test_get_url_with_existing_url():
    backend = Backend()
    project = "project_name"
    key = "thumbnail.png"
    url = f"https://{backend.cdn_url}/projects/{project}/{key}"
    with patch.object(backend, 'url_exists', return_value=True) as mock_url_exists:
        result = backend.get_url(project, key)
        assert result == url
    mock_url_exists.assert_called_once_with(url)

def test_get_url_with_non_existing_url():
    backend = Backend()
    project = "project_name"
    key = "thumbnail.png"
    with patch.object(backend, 'url_exists', return_value=False) as mock_url_exists:
        result = backend.get_url(project, key)
        assert result is None
    mock_url_exists.assert_called_once_with(url)

def test_project_dict_with_valid_project_name():
    backend = Backend()
    project_name = "project_name"
    expected_dict = {
        "thumbnail": f"https://{backend.cdn_url}/projects/{project_name}/thumbnail.png",
        "body": f"https://{backend.cdn_url}/projects/{project_name}/body.pdf",
        "slides": f"https://{backend.cdn_url}/projects/{project_name}/slides.pptx",
        "video": f"https://{backend.cdn_url}/projects/{project_name}/video.mp4",
    }
    with patch.object(backend, 'get_url', return_value=True) as mock_get_url:
        result = backend.project_dict(project_name)
        assert result == expected_dict
    assert mock_get_url.call_count == 4

def test_project_dict_with_invalid_project_name():
    backend = Backend()
    project_name = "project_name"
    with patch.object(backend, 'get_url', return_value=None) as mock_get_url:
        result = backend.project_dict(project_name)
        assert result == {}
    assert mock_get_url.call_count == 4

def test_list_projects():
    backend = Backend()
    with patch.object(backend, 'projects_dict') as mock_projects_dict:
        backend.list_projects()
    mock_projects_dict.assert_called_once()

def test_projects_dict():
    backend = Backend()
    with patch.object(backend, 'list_projects', return_value=["project1", "project2"]) as mock_list_projects:
        result = backend.projects_dict()
        assert result == ["project1", "project2"]
    mock_list_projects.assert_called_once()