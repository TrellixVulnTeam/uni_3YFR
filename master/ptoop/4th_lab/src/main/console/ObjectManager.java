package main.console;

import main.serialization.ISerializable;

import java.util.ArrayList;
import java.util.List;

public class ObjectManager {
    public List<Class<?>> types;
    public List<ISerializable> objects;

    public ObjectManager(List<Class<?>> types) {
        this(types, new ArrayList<>());
    }

    public ObjectManager(List<Class<?>> types, List<ISerializable> objects) {
        this.types = types;
        this.objects = objects;
    }
}
