provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "vuln-rg"
  location = "East US"
}

resource "azurerm_storage_account" "bad_storage" {
  name                     = "vulnstorageacct123"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  # ❌ insecure settings (Checkov should flag)
  allow_blob_public_access = true
}

resource "azurerm_storage_container" "bad_container" {
  name                  = "public-container"
  storage_account_name  = azurerm_storage_account.bad_storage.name
  container_access_type = "blob"  # ❌ public access
}