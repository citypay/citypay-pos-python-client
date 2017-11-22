# citypay.PaymentModuleApi

All URIs are relative to *https://pos.citypay.com/citypay-pos-api/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**receipt**](PaymentModuleApi.md#receipt) | **POST** /receipt | Receipt Print
[**refund**](PaymentModuleApi.md#refund) | **POST** /refund | Refund Transaction
[**reversal**](PaymentModuleApi.md#reversal) | **POST** /reversal | Reversal Tranasction
[**sale**](PaymentModuleApi.md#sale) | **POST** /sale | Sale Transaction
[**transaction**](PaymentModuleApi.md#transaction) | **POST** /transaction | Transaction Status


# **receipt**
> TransactionResult receipt(body=body)

Receipt Print

Reprint a merchant or customer receipt for a transaction that exists on the device (i.e. has not been cleared by End of Day process). 

### Example
```python
from __future__ import print_function
import time
import citypay
from citypay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = citypay.PaymentModuleApi()
body = citypay.TransactionProgress() # TransactionProgress |  (optional)

try:
    # Receipt Print
    api_response = api_instance.receipt(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentModuleApi->receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionProgress**](TransactionProgress.md)|  | [optional] 

### Return type

[**TransactionResult**](TransactionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund**
> SaleResponse refund(body)

Refund Transaction

Initiates a new refund to a device. The action will contact the device and request a transaction start including the amount and a unique reference to track the transaction through it's lifecycle. 

### Example
```python
from __future__ import print_function
import time
import citypay
from citypay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = citypay.PaymentModuleApi()
body = citypay.SaleRequest() # SaleRequest | 

try:
    # Refund Transaction
    api_response = api_instance.refund(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentModuleApi->refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SaleRequest**](SaleRequest.md)|  | 

### Return type

[**SaleResponse**](SaleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reversal**
> SaleResponse reversal(body)

Reversal Tranasction

Initiates a reversal to a device. No confirmation is made and the transaction reversal process is run. 

### Example
```python
from __future__ import print_function
import time
import citypay
from citypay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = citypay.PaymentModuleApi()
body = citypay.ReversalRequest() # ReversalRequest | 

try:
    # Reversal Tranasction
    api_response = api_instance.reversal(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentModuleApi->reversal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReversalRequest**](ReversalRequest.md)|  | 

### Return type

[**SaleResponse**](SaleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sale**
> SaleResponse sale(body)

Sale Transaction

Initiates a new sale to a device. The action will contact the device and request a transaction start including the amount and a unique reference to track the transaction through it's lifecycle. 

### Example
```python
from __future__ import print_function
import time
import citypay
from citypay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = citypay.PaymentModuleApi()
body = citypay.SaleRequest() # SaleRequest | 

try:
    # Sale Transaction
    api_response = api_instance.sale(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentModuleApi->sale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SaleRequest**](SaleRequest.md)|  | 

### Return type

[**SaleResponse**](SaleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction**
> TransactionResult transaction(body=body)

Transaction Status

Request the status of a transaction in progress or a complete transaction using the identifier as the reference. Depending on the state of the transaction, the response will indicate if it is not found, in progress (and the current stage in the transaction workflow) or complete (with all transaction data). 

### Example
```python
from __future__ import print_function
import time
import citypay
from citypay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = citypay.PaymentModuleApi()
body = citypay.TransactionProgress() # TransactionProgress |  (optional)

try:
    # Transaction Status
    api_response = api_instance.transaction(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentModuleApi->transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionProgress**](TransactionProgress.md)|  | [optional] 

### Return type

[**TransactionResult**](TransactionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

