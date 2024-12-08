import requests
import pytest
#pip install jinja2

class TestCoinDeskAPI:
    BASE_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

    def test_api_response(self):
        # 1. Sending the GET request
        response = requests.get(self.BASE_URL)
        
        # Verifying that the response is successful
        assert response.status_code == 200, "API request failed"
        
        # Parsing the JSON response
        data = response.json()
        
        # 2. Verifying BPI details and veryfying that 3 bpis exist
        bpi = data.get('bpi', {})
        assert len(bpi) == 3, f"Expected 3 BPIs, found {len(bpi)}"
        
        # Verifyin all specific BPI currencies
        expected_currencies = ['USD', 'GBP', 'EUR']
        for currency in expected_currencies:
            assert currency in bpi, f"{currency} not found in BPI"
        
        # Verify description of GBP
        gbp_bpi = bpi.get('GBP', {})
        assert gbp_bpi.get('description') == 'British Pound Sterling', \
            "GBP description does not match expected value"
        

# If running directly
if __name__ == "__main__":
    pytest.main([__file__])