from typing import TypedDict, Optional, List, Dict, Union

class UserAgent(TypedDict):
    mode: str
    value: str

class Webrtc(TypedDict):
    mode: str
    ipAddress: Optional[str]

class Canvas(TypedDict):
    mode: str

class Webgl(TypedDict):
    mode: str

class WebglInfo(TypedDict):
    mode: str
    vendor: str
    renderer: str

class ClientRect(TypedDict):
    mode: str

class Notes(TypedDict):
    content: str
    color: str
    style: str
    icon: str

class Timezone(TypedDict):
    mode: str
    value: Optional[str]

class Locale(TypedDict):
    mode: str
    value: Optional[str]

class Geolocation(TypedDict):
    mode: str
    latitude: Optional[float]
    longitude: Optional[float]
    accuracy: Optional[float]

class CPU(TypedDict):
    mode: str
    value: int

class Memory(TypedDict):
    mode: str
    value: int

class Screen(TypedDict):
    mode: str
    resolution: Optional[str]

class Ports(TypedDict):
    mode: str
    blacklist: str

class Access(TypedDict):
    view: int
    update: int
    delete: int
    share: int
    usage: int

class MediaDevices(TypedDict):
    mode: str
    audioInputs: Optional[str]
    videoInputs: Optional[str]
    audioOutputs: Optional[str]

class WebGPU(TypedDict):
    mode: str
    value: str

class UserProfile(TypedDict):
    id: int
    userId: int
    teamId: int
    name: str
    platform: str
    browserType: str
    proxyId: int
    mainWebsite: str
    useragent: UserAgent
    webrtc: Webrtc
    canvas: Canvas
    webgl: Webgl
    webglInfo: WebglInfo
    clientRect: ClientRect
    notes: Notes
    timezone: Timezone
    locale: Locale
    totalSessionDuration: int
    userFields: str
    geolocation: Geolocation
    doNotTrack: bool
    args: List[str]
    cpu: CPU
    memory: Memory
    screen: Screen
    ports: Ports
    tabs: List[str]
    created_at: str
    updated_at: str
    deleted_at: str
    platformName: str
    cpuArchitecture: str
    osVersion: int
    screenWidth: Optional[str]
    screenHeight: Optional[str]
    connectionDownlink: int
    connectionEffectiveType: str
    connectionRtt: int
    connectionSaveData: int
    vendorSub: str
    productSub: int
    vendor: str
    product: str
    appCodeName: str
    mediaDevices: MediaDevices
    datadirHash: Optional[str]
    cookiesHash: Optional[str]
    storagePath: str
    platformVersion: str
    extensionsNewNaming: int
    archived: int
    webgl2Maximum: Optional[str]
    login: Optional[str]
    password: Optional[str]
    sortingName: str
    addedSortingName: int
    access: Access
    transfer: int
    webgpu: WebGPU
    recoverCount: Optional[str]
    lastStartTime: str
    proxy: Dict[str, int]
    sorting_name: str
    status: Dict[str, Union[int, str]]
    macAddress: Dict[str, Optional[str]]
    deviceName: Dict[str, Optional[str]]
    isHiddenProfileName: int
    tags: List[str]
    tags_with_separator: List[str]
    pinned: bool
    folder: int
    transferToEmail: str
    transferStatus: str
    transferHandleDate: str
    transferWithProxy: str
    homepages: List[Dict[str, Union[int, str]]]
