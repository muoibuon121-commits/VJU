``` mermaid
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'primaryColor': '#E1F5FE',
    'primaryTextColor': '#01579B',
    'primaryBorderColor': '#0288D1',
    'lineColor': '#0288D1',
    'fontFamily': 'Arial',
    'clusterBkg': '#FFFFFF'
  }
}}%%
mindmap
  root((b2b_invoice_system))
    manage.py
    requirements.txt
    docker-compose.yml
    config
      settings.py
      urls.py
      wsgi.py
    apps
      users
        models.py
        views.py
        serializers.py
        urls.py
      customers
        models.py
        views.py
        serializers.py
        admin.py
      products
        models.py
        views.py
        serializers.py
      invoices
        models.py
        views.py
        serializers.py
        services.py
        urls.py
      contracts
        models.py
        views.py
        serializers.py
        services.py
    tests
      test_models.py
      test_views.py
