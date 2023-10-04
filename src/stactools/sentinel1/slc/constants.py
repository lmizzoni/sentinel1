from datetime import datetime
from typing import Dict, Any

import pystac
from pystac import Extent, ProviderRole, SpatialExtent, TemporalExtent
from pystac.link import Link
from pystac.extensions import sar, sat
from pystac.utils import str_to_datetime
from pystac.extensions.item_assets import AssetDefinition

from ..constants import *


SENTINEL_SLC_DESCRIPTION = (
    "Level-1 Single Look Complex (SLC) products are images in the slant range by azimuth imaging plane, in the image plane of satellite data acquisition. Each image pixel is represented by a complex (I and Q) magnitude value and therefore contains both amplitude and phase information. Each I and Q value "  # noqa: E501
    "is 16 bits per pixel. The processing for all SLC products results in a single look in each dimension using the full available signal bandwidth. The imagery is geo-referenced using orbit and attitude data from the satellite. SLC images are produced in a zero Doppler geometry. This convention is common "  # noqa: E501
    "with the standard slant range products available from other SAR sensors."
)

SENTINEL_SLC_START: datetime = str_to_datetime("2014-10-10T00:00:00Z")
SENTINEL_SLC_EXTENT = Extent(
    SpatialExtent([-180.0, -90.0, 180.0, 90.0]),
    TemporalExtent([[SENTINEL_SLC_START, None]]),
)

SENTINEL_SLC_TECHNICAL_GUIDE = Link(
    title="Sentinel-1 Single Look Complex (SLC) Technical Guide",
    rel="about",
    target="https://sentinels.copernicus.eu/web/sentinel/technical-guides/sentinel-1-sar/products-algorithms/level-1-algorithms/single-look-complex",  # noqa: E501
)

SENTINEL_SLC_LICENSE = Link(
    title="Sentinel License",
    rel="license",
    target="https://scihub.copernicus.eu/twiki/do/view/SciHubWebPortal/TermsConditions",
)

SENTINEL_SLC_KEYWORDS = ["ground", "sentinel", "copernicus", "esa", "sar"]

SENTINEL_SLC_SAT = {
    "orbit_state": [sat.OrbitState.ASCENDING, sat.OrbitState.DESCENDING]
}

SENTINEL_SLC_SAR: Dict[str, Any] = {
    "looks_range": [1],
    "product_type": ["SLC"],
    "looks_azimuth": [1],
    "polarizations": [
        sar.Polarization.HH,
        sar.Polarization.VV,
        sar.Polarization.HV,
        sar.Polarization.VH,
        [
            sar.Polarization.HH,
            sar.Polarization.HV,
        ],
        [
            sar.Polarization.VV,
            sar.Polarization.VH,
        ],
    ],
    "frequency_band": [sar.FrequencyBand.C],
    "instrument_mode": ["IW", "EW", "SM", "WV"],
    "center_frequency": [5.405],
    "resolution_range": [
        1.7,
        2.0,
        2.5,
        2.7,
        3.1,
        3.3,
        3.6,
        3.5,
        7.9,
        9.9,
        11.6,
        13.3,
        14.4,
    ],
    "resolution_azimuth": [
        3.9,
        4.9,
        22.5,
        22.6,
        22.7,
        43.7,
        44.3,
        45.2,
        45.6,
        44.0,
    ],
    "pixel_spacing_range": [
        1.5,
        1.8,
        2.2,
        2.3,
        2.6,
        2.9,
        3.1,
        5.9,
    ],
    "pixel_spacing_azimuth": [
        3.5,
        3.6,
        4.1,
        4.2,
        14.1,
        19.9,
    ],
    "observation_direction": [sar.ObservationDirection.RIGHT],
    "looks_equivalent_number": [1],
}


SENTINEL_SLC_ASSETS = {
    "vh": AssetDefinition(
        {
            "title": "VH Data",
            "type": pystac.MediaType.COG,
            "description": "VH polarization backscattering coefficient, 16-bit DN.",
            "roles": ["data"],
        }
    ),
    "hh": AssetDefinition(
        {
            "title": "HH Data",
            "type": pystac.MediaType.COG,
            "description": "HH polarization backscattering coefficient, 16-bit DN.",
            "roles": ["data"],
        }
    ),
    "hv": AssetDefinition(
        {
            "title": "HV Data",
            "type": pystac.MediaType.COG,
            "description": "HV polarization backscattering coefficient, 16-bit DN.",
            "roles": ["data"],
        }
    ),
    "vv": AssetDefinition(
        {
            "title": "VV Data",
            "type": pystac.MediaType.COG,
            "description": "VV polarization backscattering coefficient, 16-bit DN.",
            "roles": ["data"],
        }
    ),
    "schema-calibration-hh": AssetDefinition(
        {
            "title": "HH Calibration Schema",
            "type": pystac.MediaType.XML,
            "description": (
                "Calibration metadata including calibration information and the beta nought, "
                "sigma nought, gamma and digital number look-up tables that can be used for "
                "absolute product calibration."
            ),
            "roles": ["metadata"],
        }
    ),
    "schema-calibration-hv": AssetDefinition(
        {
            "title": "HV Calibration Schema",
            "type": pystac.MediaType.XML,
            "description": (
                "Calibration metadata including calibration information and the beta nought, "
                "sigma nought, gamma and digital number look-up tables that can be used for "
                "absolute product calibration."
            ),
            "roles": ["metadata"],
        }
    ),
    "schema-calibration-vh": AssetDefinition(
        {
            "title": "VH Calibration Schema",
            "type": pystac.MediaType.XML,
            "description": (
                "Calibration metadata including calibration information and the beta nought, "
                "sigma nought, gamma and digital number look-up tables that can be used for "
                "absolute product calibration."
            ),
            "roles": ["metadata"],
        }
    ),
    "schema-calibration-vv": AssetDefinition(
        {
            "title": "VV Calibration Schema",
            "type": pystac.MediaType.XML,
            "description": (
                "Calibration metadata including calibration information and the beta nought, "
                "sigma nought, gamma and digital number look-up tables that can be used for "
                "absolute product calibration."
            ),
            "roles": ["metadata"],
        }
    ),
    "schema-noise-hh": AssetDefinition(
        {
            "title": "HH Noise Schema",
            "type": pystac.MediaType.XML,
            "description": "Estimated thermal noise look-up tables",
            "roles": ["metadata"],
        }
    ),
    "schema-noise-hv": AssetDefinition(
        {
            "title": "HV Noise Schema",
            "type": pystac.MediaType.XML,
            "description": "Estimated thermal noise look-up tables",
            "roles": ["metadata"],
        }
    ),
    "schema-noise-vh": AssetDefinition(
        {
            "title": "VH Noise Schema",
            "type": pystac.MediaType.XML,
            "description": "Estimated thermal noise look-up tables",
            "roles": ["metadata"],
        }
    ),
    "schema-noise-vv": AssetDefinition(
        {
            "title": "VV Noise Schema",
            "type": pystac.MediaType.XML,
            "description": "Estimated thermal noise look-up tables",
            "roles": ["metadata"],
        }
    ),
    "schema-product-hh": AssetDefinition(
        {
            "title": "HH Product Schema",
            "type": pystac.MediaType.XML,
            "description": (
                "Describes the main characteristics corresponding to the band: state of the "
                "platform during acquisition, image properties, Doppler information, geographic "
                "location, etc."
            ),
            "roles": ["metadata"],
        }
    ),
    "schema-product-hv": AssetDefinition(
        {
            "title": "HV Product Schema",
            "type": pystac.MediaType.XML,
            "description": (
                "Describes the main characteristics corresponding to the band: state of the "
                "platform during acquisition, image properties, Doppler information, geographic "
                "location, etc."
            ),
            "roles": ["metadata"],
        }
    ),
    "schema-product-vh": AssetDefinition(
        {
            "title": "VH Product Schema",
            "type": pystac.MediaType.XML,
            "description": (
                "Describes the main characteristics corresponding to the band: state of the "
                "platform during acquisition, image properties, Doppler information, geographic "
                "location, etc."
            ),
            "roles": ["metadata"],
        }
    ),
    "schema-product-vv": AssetDefinition(
        {
            "title": "VV Product Schema",
            "type": pystac.MediaType.XML,
            "description": (
                "Describes the main characteristics corresponding to the band: state of the "
                "platform during acquisition, image properties, Doppler information, geographic "
                "location, etc."
            ),
            "roles": ["metadata"],
        }
    ),
    "safe-manifest": AssetDefinition(
        {
            "title": "Manifest File",
            "type": pystac.MediaType.XML,
            "description": (
                "General product metadata in XML format. Contains a high-level textual "
                "description of the product and references to all of product's components, "
                "the product metadata, including the product identification and the resource "
                "references, and references to the physical location of each component file "
                "contained in the product."
            ),
            "roles": ["metadata"],
        }
    ),
    "thumbnail": AssetDefinition(
        {
            "title": "Preview Image",
            "type": pystac.MediaType.PNG,
            "description": (
                "An averaged, decimated preview image in PNG format. Single polarization "
                "products are represented with a grey scale image. Dual polarization products "
                "are represented by a single composite colour image in RGB with the red channel "
                "(R) representing the  co-polarization VV or HH), the green channel (G) "
                "represents the cross-polarization (VH or HV) and the blue channel (B) "
                "represents the ratio of the cross an co-polarizations."
            ),
            "roles": ["thumbnail"],
        }
    ),
}


SENTINEL_SLC_IW_TPRE = 2.299849  # Preamble length
SENTINEL_SLC_IW_TBEAM = 2.758273  # Beam cycle time
SENTINEL_SLC_IW_TORB = 12 * 86400 / 175  # Nominal orbit duration

SENTINEL_SLC_EW_TPRE = 2.299970  # Preamble length
SENTINEL_SLC_EW_TBEAM = 3.038376  # Beam cycle time
SENTINEL_SLC_EW_TORB = 12 * 86400 / 175  # Nominal orbit duration
