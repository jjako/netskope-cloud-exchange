{
  "name": "Jason_demo",
  "id": "jason_demo",
  "version": "1.0.0",
  "description": "Write user risk scores.",
  "type": ["user"],
  "netskope": false,
  "configuration": [
    {
      "label": "Base URL",
      "key": "url",
      "type": "text",
      "default": "https://bogus.com",
      "mandatory": true,
      "description": "bogus link not used."
    },
    {
      "label": "Application ID",
      "key": "app_id",
      "type": "text",
      "mandatory": true,
      "description": "bogus Application ID."
    },
    {
      "label": "Application Key",
      "key": "app_key",
      "type": "password",
      "mandatory": true,
      "description": "bogus API Application Key."
    },
    {
      "label": "Access Key",
      "key": "access_key",
      "type": "password",
      "mandatory": true,
      "description": "bogus user's access key."
    },
    {
      "label": "Secret Key",
      "key": "secret_key",
      "type": "password",
      "mandatory": true,
      "description": "bogus user's secret key."
    }
  ]
}
