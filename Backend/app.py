import os
from dotenv import load_dotenv
import aiohttp
import asyncio
import re
import math
from datetime import datetime
from fastapi import FastAPI, File, UploadFile, HTTPException, Form, Query
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil
import logging
from tempfile import NamedTemporaryFile
from pic_to_3d import process_image_get_depth_data, depth_data_to_3d_model
import numpy as np
from PIL import Image