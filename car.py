from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from OpenGL.GL import *
import math

class Test(Base):
    def initialize(self):
        print("init")

        # Vertex Shader
        vsCode = """
        in vec3 position;
        void main(){
            gl_Position = vec4(position, 1.0);
        }
        """

        # Fragment Shader (oranye)
        fsCode = """
        out vec4 fragColor;
        void main(){
            fragColor = vec4(1.0, 0.5, 0.0, 1.0);
        }
        """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)
        glLineWidth(4)

        # =======================================
        # 1. BODY MOBIL (persegi panjang)
        # =======================================
        self.vaoBody = glGenVertexArrays(1)
        glBindVertexArray(self.vaoBody)

        bodyData = [
            [-0.6, -0.2, 0.0],
            [ 0.6, -0.2, 0.0],
            [ 0.6,  0.2, 0.0],
            [-0.6,  0.2, 0.0]
        ]

        self.bodyCount = len(bodyData)
        bodyAttr = Attribute("vec3", bodyData)
        bodyAttr.associateVariable(self.programRef, "position")

        # =======================================
        # 2. ATAP MOBIL (trapesium)
        # =======================================
        self.vaoRoof = glGenVertexArrays(1)
        glBindVertexArray(self.vaoRoof)

        roofData = [
            [-0.3,  0.2, 0.0],
            [ 0.3,  0.2, 0.0],
            [ 0.15, 0.5, 0.0],
            [-0.15, 0.5, 0.0]
        ]

        self.roofCount = len(roofData)
        roofAttr = Attribute("vec3", roofData)
        roofAttr.associateVariable(self.programRef, "position")

        # =======================================
        # 3. RODA KIRI (lingkaran 32 titik)
        # =======================================
        self.vaoWheelLeft = glGenVertexArrays(1)
        glBindVertexArray(self.vaoWheelLeft)

        wheelLeftData = []
        cx, cy = -0.3, -0.2   # posisi roda kiri
        r = 0.15              # radius roda

        for i in range(32):
            angle = 2 * math.pi * i / 32
            wheelLeftData.append([
                cx + r * math.cos(angle),
                cy + r * math.sin(angle),
                0.0
            ])

        self.leftWheelCount = len(wheelLeftData)
        wheelLeftAttr = Attribute("vec3", wheelLeftData)
        wheelLeftAttr.associateVariable(self.programRef, "position")

        # =======================================
        # 4. RODA KANAN
        # =======================================
        self.vaoWheelRight = glGenVertexArrays(1)
        glBindVertexArray(self.vaoWheelRight)

        wheelRightData = []
        cx2, cy2 = 0.3, -0.2  # posisi roda kanan

        for i in range(32):
            angle = 2 * math.pi * i / 32
            wheelRightData.append([
                cx2 + r * math.cos(angle),
                cy2 + r * math.sin(angle),
                0.0
            ])

        self.rightWheelCount = len(wheelRightData)
        wheelRightAttr = Attribute("vec3", wheelRightData)
        wheelRightAttr.associateVariable(self.programRef, "position")

    def update(self):
        glUseProgram(self.programRef)

        # Body mobil
        glBindVertexArray(self.vaoBody)
        glDrawArrays(GL_LINE_LOOP, 0, self.bodyCount)

        # Atap mobil
        glBindVertexArray(self.vaoRoof)
        glDrawArrays(GL_LINE_LOOP, 0, self.roofCount)

        # Roda kiri
        glBindVertexArray(self.vaoWheelLeft)
        glDrawArrays(GL_LINE_LOOP, 0, self.leftWheelCount)

        # Roda kanan
        glBindVertexArray(self.vaoWheelRight)
        glDrawArrays(GL_LINE_LOOP, 0, self.rightWheelCount)

Test().run()
