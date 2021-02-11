Simple utility for patching the original `debugserver` which comes with XCode in include entitlements
for debugging other processes in a jailbroken device.

The binary can be obtained from:

`/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport/<IOS_VERSION>/DeveloperDiskImage.dmg`

Just replace the `<IOS_VERSION>` with your correct version.

In order to patch, please run as follows:

```shell
./main.py original_debugserver patched_debugserver
```
