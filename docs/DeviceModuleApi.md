# citypay.DeviceModuleApi

All URIs are relative to *https://pos.citypay.com/citypay-pos-api/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_info**](DeviceModuleApi.md#device_info) | **GET** /device/{deviceId}/info | Device Information
[**ping**](DeviceModuleApi.md#ping) | **GET** /device/{deviceId}/ping | Device Ping


# **device_info**
> DeviceInfo device_info(device_id)

Device Information

Obtains information regarding the device and to review the current status of a device such as the battery charge, serial number and device type. 

### Example
```python
from __future__ import print_function
import time
import citypay
from citypay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = citypay.DeviceModuleApi()
device_id = 'device_id_example' # str | The name of the target device used by the API.

try:
    # Device Information
    api_response = api_instance.device_info(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceModuleApi->device_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| The name of the target device used by the API. | 

### Return type

[**DeviceInfo**](DeviceInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping**
> Result ping(device_id)

Device Ping

To monitor or to check whether a device is available, the host can send a simple `GET` request to the URL at `/device/{deviceId}/ping` to see if the device is responding and available. 

### Example
```python
from __future__ import print_function
import time
import citypay
from citypay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = citypay.DeviceModuleApi()
device_id = 'device_id_example' # str | The name of the target device used by the API.

try:
    # Device Ping
    api_response = api_instance.ping(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceModuleApi->ping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| The name of the target device used by the API. | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

