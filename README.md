# IP Geo Location MCP Server

## Overview

The IP Geo Location MCP Server is a powerful tool designed to provide detailed geographical information based on IP addresses. This service is particularly useful for developers and businesses looking to enhance their applications and services with location-based insights.

## Key Features

- **Detailed Location Data**: Retrieve comprehensive information about a visitor's geographic location, including details such as country, city, latitude, longitude, timezone, ASN (Autonomous System Number), currency, and security data.
  
- **IP Address Support**: The server supports both IPv4 and IPv6 addresses, ensuring compatibility with the latest internet protocols.
  
- **Multiple Response Formats**: Data can be returned in either JSON or XML format, allowing for easy integration into various applications and systems.
  
- **Language Support**: The service supports a wide range of languages including English, Russian, Chinese, Spanish, Arabic, French, Persian, Japanese, Polish, Italian, Portuguese, and German. This feature allows users to receive location data in their preferred language.
  
- **Customizable Data Filtering**: Users can filter the response to receive only the data they require. Available filters include ASN, city, country, continent, area, currency, security, time, and postcode.

## Usage

The IP Geo Location MCP Server provides two primary tools:

1. **Visitor Lookup**: 
   - Description: Returns the IP address of the client along with all relevant location data.
   - Parameters:
     - `format` (optional): The desired format of the data (JSON or XML).
     - `filter` (optional): Allows you to specify which data points you want to receive. Options include ASN, city, country, continent, area, currency, security, time, and postcode.
     - `language` (optional): The language code for the results. Available options are: en, ru, zh, es, ar, fr, fa, ja, pl, it, pt, de.

2. **IP Lookup**:
   - Description: Provides geographical information for a specified IP address.
   - Parameters:
     - `format` (optional): The desired format of the data (JSON or XML).
     - `filter` (optional): Allows you to specify which data points you want to receive. Options include ASN, city, country, continent, area, currency, security, time, and postcode.
     - `language` (optional): The language code for the results. Available options are: en, ru, zh, es, ar, fr, fa, ja, pl, it, pt, de.

## Error Handling

The server provides structured error responses in case of failed requests or unavailable resources. Common error codes include:

- **400**: Bad request.
- **403**: Authentication failed.
- **404**: Resource not found or incorrect format requested.
- **405**: Method not allowed.
- **500**: Server error (rare occurrence).

This server is a reliable choice for integrating IP-based location data into your applications, offering a robust set of features and tools to meet diverse needs.