#!/usr/bin/env python3

import argparse
import csv
import random
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="Asignar estudiantes a grupos aleatorios y generar un archivo CSV de salida."
    )
    parser.add_argument(
        "--seed",
        "-s",
        type=int,
        default=None,
        help="Semilla aleatoria inicial. Si no se indica, se elige una semilla aleatoria.",
    )
    parser.add_argument(
        "--file",
        "-f",
        required=True,
        help="Archivo de texto plano con los nombres de los estudiantes.",
    )
    parser.add_argument(
        "--remove-header",
        "-r",
        action="store_true",
        help="Ignora la primera fila del archivo de estudiantes si contiene encabezado.",
    )
    parser.add_argument(
        "--group",
        "-g",
        type=int,
        required=True,
        help="Tamaño del grupo.",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="groups.csv",
        help="Nombre del archivo CSV de salida.",
    )
    return parser.parse_args()


def read_students(file_path, remove_header=False):
    try:
        with open(file_path, encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{file_path}'.", file=sys.stderr)
        sys.exit(1)

    if not lines:
        print(f"Error: el archivo '{file_path}' está vacío.", file=sys.stderr)
        sys.exit(1)

    if remove_header:
        return lines[1:]

    return lines


def write_groups(output_path, students, group_size):
    with open(output_path, mode="w", newline="", encoding="utf-8") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["student", "group"])
        for index, student in enumerate(students):
            group_number = index // group_size + 1
            writer.writerow([student, group_number])


def main():
    args = parse_args()

    if args.group <= 0:
        print("Error: el tamaño del grupo debe ser un número entero mayor que 0.", file=sys.stderr)
        sys.exit(1)

    students = read_students(args.file, remove_header=args.remove_header)

    if not students:
        print("Error: no hay estudiantes para asignar.", file=sys.stderr)
        sys.exit(1)

    if args.seed is None:
        seed = random.SystemRandom().randint(0, 2**32 - 1)
        print(f"Semilla elegida aleatoriamente: {seed}")
    else:
        seed = args.seed
        print(f"Semilla fija utilizada: {seed}")

    rng = random.Random(seed)
    rng.shuffle(students)

    write_groups(args.output, students, args.group)
    print(f"Archivo CSV generado: {args.output}")


if __name__ == "__main__":
    main()
