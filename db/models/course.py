from datetime import datetime
import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URL_type

from ..db_setup import Base
from user import User
from mixins import Timestamp

class ContentType(enum.Enum):
    lesson = 1
    quiz = 2
    assignment = 3
    
class Course(Timestamp, Base):
    __tablename__= "courses"
    
    
    id = Column(Integer, primary_key=True, index = True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    
    created_by = relationship(User)
    sections = relationship("Section", back_populates="course", uselist=False)
    student_courses = relationship("StudentCourse", back_populates="course")
    
    
class Section(Timestamp, Base):
    __tablename__ = "sections"
    
    id = Column(Integer, primary_key=True, index = True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    
    course = relationship("Course", back_populates="sections")
    content_blocks = relationship("ContentBlock", back_populates="section")
    
class ContentBlock(Timestamp, Base):
    __tablename__ = "content_blocks"
    
    id = Column(Integer, primary_key=True, index = True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    type = Column(Enum(ContentType))
    url = Column(URL_type, nullable=True)
    content = Column(Text, nullable=True)
    
    section = relationship("Section", back_populates="content_blocks")
    completed_content_blocks = relationship("CompletedContentBlock", back_populates="content_block")
    
    
class StudentCourse(Timestamp, Base):
    """
    Students can be assigned to courses
    """
    __tablename__ = "student_course"
    
    id = Column(Integer, primary_key=True, index = True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
                                            